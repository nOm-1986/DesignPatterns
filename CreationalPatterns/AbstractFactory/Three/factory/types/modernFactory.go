package types

type Modern struct{}

func (m *Modern) MakeChair() IChair {
	return &ModernChair{
		Chair: Chair{
			tipo: "Modern",
			size: "Media",
			legs: 4,
		},
	}
}

func (m *Modern) MakeSofa() ISofa {
	return &ModernSofa{
		Sofa: Sofa{
			tipo: "Modern",
			size: "height 80, width 1mt and length 1.8mts",
			legs: 4,
		},
	}
}

func (m *Modern) MakeTable() ITable {
	return &ModernTable{
		Table: Table{
			tipo: "Modern",
			size: "height 85, width 1.2mt and length 1.8mts",
			legs: 4,
		},
	}
}
