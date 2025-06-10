package types

import "fmt"

func GetGun(typeG string) (IGun, error) {
	switch typeG {
	case "ak47":
		return NewAk47(), nil
	case "musket":
		return &Musket{name: "musket", power: 6}, nil
	default:
		return nil, fmt.Errorf("wrong gun type passed")
	}
}
