package types

type Gun struct {
	name  string
	power int
}

func (g *Gun) setName(nameS string) {
	g.name = nameS
}

func (g *Gun) setPower(p int) {
	g.power = p
}

func (g Gun) GetName() string {
	return g.name
}

func (g Gun) GetPower() int {
	return g.power
}
