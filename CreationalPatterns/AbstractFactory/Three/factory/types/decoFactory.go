package types

type Deco struct{}

func (Deco) MakeChair() IChair {
	return &decoChair{
		Chair: Chair{
			tipo: "Art Deco",
			size: "Media",
			legs: 4,
		},
	}
}

func (Deco) MakeSofa() ISofa {
	return &decoSofa{
		tipo: "Art Deco",
		size: "height 80, width 1mt and length 1.8mts",
		legs: 4,
	}
}

func (Deco) MakeTable() ITable {
	return &decoTable{
		Table: Table{
			tipo: "Art Deco",
			size: "height 85, width 1.2mt and length 1.8mts",
			legs: 4,
		},
	}
}
