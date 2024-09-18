package types

type Ak47 struct {
	Gun
}

func NewAk47() IGun {
	return &Ak47{
		Gun: Gun{
			name:  "Ak47",
			power: 5,
		},
	}
}
