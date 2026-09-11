"""Verify the final Tuza certificate on Linux (Python 3.10+ and NumPy)."""
import gzip
import itertools as it
import json
from pathlib import Path

def require(ok, message):
    if not ok: raise ValueError(message)

def signature(masks):
    # Canonical multiset of membership words; independent of count-vector code.
    return min(tuple(sorted(tuple(int(bool(masks[j] & (1 << v))) for j in perm)
                            for v in range(8))) for perm in it.permutations(range(3)))


def graph(masks, counts):
    edges = set(it.combinations(range(8), 2))
    triangles = list(it.combinations(range(8), 3))
    vertex = 8
    for mask, multiplicity in zip(masks,counts):
        neighbors = [i for i in range(8) if mask & (1 << i)]
        for _ in range(multiplicity):
            edges.update((u,vertex) for u in neighbors)
            triangles.extend((u,v,vertex) for u,v in it.combinations(neighbors,2))
            vertex += 1
    return edges, triangles


def tuza(artifact, target_signatures):
    import numpy as np
    require(len(target_signatures) == 560, 'target identity audit')
    seen = set(); boxes = 0; complete = 0; incomplete = []
    for p in artifact['profiles']:
        masks = p['masks']
        require(len(masks)==3 and all(type(m) is int and 0<=m<256 for m in masks), 'masks')
        s = signature(masks)
        require(s in target_signatures and s not in seen, 'profile identity/duplicate')
        seen.add(s)
        covered = np.zeros((29,29,29), dtype=bool)
        for b in p['boxes']:
            lo,hi = b['lo'],b['hi']
            require(len(lo)==len(hi)==3 and all(type(v) is int for v in lo+hi), 'box dimension')
            require(all(0<=l<=h<=28 for l,h in zip(lo,hi)), 'box range')
            top_edges, top_triangles = graph(masks,hi)
            cover = {tuple(sorted(e)) for e in b['cover']}
            require(len(cover)==len(b['cover']) and cover<=top_edges, 'invalid cover edges')
            for t in top_triangles:
                require(any(e in cover for e in it.combinations(t,2)), 'uncovered triangle')
            bottom_edges,_ = graph(masks,lo)
            used = set()
            for t in b['packing']:
                require(len(t)==3 and len(set(t))==3, 'packing triangle')
                te = set(it.combinations(sorted(t),2))
                require(te<=bottom_edges and not (te & used), 'invalid/shared packing edge')
                used |= te
            require(len(cover) <= 2*len(b['packing']), 'Tuza inequality')
            covered[tuple(slice(l,h+1) for l,h in zip(lo,hi))] = True
            boxes += 1
        if bool(covered.all()):
            complete += 1
        else:
            incomplete.append({'masks':masks,'uncovered_points':int((~covered).sum())})
    return {'complete_profiles':complete, 'submitted_profiles':len(seen),
            'target_profiles':560, 'checked_boxes':boxes, 'incomplete':incomplete,
            'scope':'Each listed complete profile covers every multiplicity in [0,28]^3; extending to all multiplicities additionally uses the truncation lemma.'}


def remaining_classes():
    seen=set(); targets=set(); counts={'nested':0,'clique_cut':0}
    for words in it.combinations_with_replacement(range(8),8):
        masks=[sum(1<<v for v,word in enumerate(words) if word & (1<<j)) for j in range(3)]
        if len(set(masks))<3 or any(m.bit_count()<2 for m in masks):continue
        s=signature(masks)
        if s in seen:continue
        seen.add(s)
        if all((a&b) in [a,b] for a,b in it.combinations(masks,2)):
            counts['nested']+=1;continue
        complement=[(u,v) for u,v in it.combinations(range(8),2)
                    if not any((m & (1<<u)) and (m & (1<<v)) for m in masks)]
        maxcut=max(sum(bool(cut&(1<<u))!=bool(cut&(1<<v)) for u,v in complement) for cut in range(128))
        if maxcut>=12:counts['clique_cut']+=1;continue
        targets.add(s)
    require(len(seen)==872 and counts=={'nested':35,'clique_cut':277} and len(targets)==560,'classification')
    return targets

if __name__=='__main__':
    import sys
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('certificate.json.gz')
    raw=path.read_bytes();artifact=json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
    result=tuza(artifact,remaining_classes())
    require(result['complete_profiles']==560 and not result['incomplete'],'incomplete proof')
    print(json.dumps({'valid':True,'classified_profiles':872,'certified_profiles':560,'boxes':result['checked_boxes']}))
