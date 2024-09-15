package types

type Victorian struct{}

func (v *Victorian) MakeChair() IChair {
	return &victorianChari{
		Chair: Chair{
			tipo: "Victoriana",
			size: "Alto 0.79mt, ancho 1mt y largo 1.7mts",
			legs: 4,
		},
	}
}

func (v *Victorian) MakeSofa() ISofa {
	return &victorianSofa{
		Sofa: Sofa{
			tipo: "Victoriana",
			size: "height 80, width 1mt and length 1.8mts",
			legs: 4,
		},
	}
}

func (m *Victorian) MakeTable() ITable {
	return &victorianTable{
		Table: Table{
			tipo: "Victoriana",
			size: "height 85, width 1.2mt and length 1.8mts",
			legs: 4,
		},
	}
}
