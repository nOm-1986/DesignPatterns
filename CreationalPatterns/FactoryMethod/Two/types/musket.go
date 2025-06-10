package types

type Musket struct {
	name  string
	power int
}

func (g *Musket) setName(nameS string) {
	g.name = nameS
}

func (g *Musket) setPower(p int) {
	g.power = p
}

func (g Musket) GetName() string {
	return g.name
}

func (g Musket) GetPower() int {
	return g.power
}

func NewMusket() IGun {
	return &Musket{
		name:  "Musket",
		power: 5,
	}
}
