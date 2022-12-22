
En Python es poden usar alies per als tipus:

```python
Player = Dict[str, Any]
Score = int

def scores(players: List[Player]) -> List[Score]
(edited)
```

i així tens documentat què rep i què retorna la funció, i tens una anotació de quina estructura espera cada concepte
i, si mai et dóna per usar objectes com a estructures de dades, ja tens la base feta
https://github.com/arnau/registers-cli