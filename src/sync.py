"""Sincroniza dados de exemplo offline. Nao faz chamadas a APIs reais."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'data' / 'proposals.csv'
DESTINATION = ROOT / 'data' / 'scores-output.csv'

with SOURCE.open(newline='', encoding='utf-8') as source, DESTINATION.open('w', newline='', encoding='utf-8') as target:
    reader = csv.DictReader(source)
    writer = csv.DictWriter(target, fieldnames=['proposal_id', 'source', 'score', 'status'])
    writer.writeheader()
    for item in reader:
        score = int(item['score'])
        writer.writerow({'proposal_id': item['proposal_id'], 'source': 'AgRisk', 'score': score, 'status': 'review' if score < 700 else 'ready'})
print(f'Arquivo gerado: {DESTINATION}')
