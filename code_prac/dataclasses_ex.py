from dataclasses import dataclass, astuple, asdict

@dataclass(frozen=True, order=True)
class DtaEx:
    id:int
    name:str


x = DtaEx(1, "Vinod Vukkalam")
print(x.id, x.name)
print(astuple(x))
print(asdict(x))
