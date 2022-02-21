Exercício 1: Em um contexto de orientação a objetos, como podemos definir o que são mensagens e qual a sua importância?

Mensagem é a comunicação entre objetos, por exemplo:
```
class FootballPlayer:
    def __init__(self, team, age, name, position):
        self.team =  team
        self.age =  age
        self.name =  name
        self.position =  position


rogerio_ceni = FootballPlayer(
                  team="SPFC",
                  age=42,
                  name="Rogerio Ceni",
                  position="goalkeeper"
)
```

A instancia `rogerio_ceni` esta mandando uma mensagem a classe `FootballPlayer`, e quando essa chamada se encerrar, nós teremos uma instancia da classe `FootballPlayer` sendo `rogerio_ceni`.

A importancia de uma mensagem é que ela é a comunicação entre uma instancia e a sua classe.