#!/usr/bin/env python3
"""Regenerate manifest.json from all .bp.json files in snapshots/"""
import glob
import json
from datetime import date

snapshots = []
for f in sorted(glob.glob('snapshots/**/*.bp.json', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fh:
        d = json.load(fh)
    snapshots.append({
        'id': d['id'],
        'technique': d['technique'],
        'severity': d['severity'],
        'path': f,
        'source': d.get('source', ''),
    })

tech_counts = {}
sev_counts = {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
for s in snapshots:
    tech_counts[s['technique']] = tech_counts.get(s['technique'], 0) + 1
    sev_counts[s['severity']] = sev_counts.get(s['severity'], 0) + 1

manifest = {
    'manifest_version': '1.0',
    'last_updated': str(date.today()),
    'total_snapshots': len(snapshots),
    'snapshots': snapshots,
    'technique_counts': tech_counts,
    'severity_counts': sev_counts,
}

with open('manifest.json', 'w', encoding='utf-8') as fh:
    json.dump(manifest, fh, indent=2)
    fh.write('\n')

print(f'manifest.json updated: {len(snapshots)} snapshots')
