# Log File Analyzer (Python, OOP)

Proiect minimal pentru tema: analizează fișiere `.log`, extrage nivele (INFO/ERROR/WARNING),
timestamp-uri, permite filtrare, export JSON și face un grafic simplu cu `matplotlib`.

## Structură
- `main.py` - CLI entrypoint
- `parser.py` - `LogParser` (parsează linii log)
- `analyzer.py` - `LogAnalyzer` (statistici, filtrare, export JSON)
- `visualizer.py` - `Visualizer` (grafic frecvență)
- `utils.py` - funcții utilitare
- `requirements.txt` - pachete
- `sample_logs/sample.log` - fișier de test

## Instalare
```bash
python -m venv venv
source venv/bin/activate   # sau venv\Scripts\activate pe Windows
pip install -r requirements.txt
```

## Exemplu de utilizare
```bash
python main.py sample_logs/sample.log --export results.json --plot
```
