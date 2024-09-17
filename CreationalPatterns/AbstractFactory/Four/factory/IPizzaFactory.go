package factory

import (
	"errors"
	. "pizzaFactory/factory/types"
)

type IPizzaFactory interface {
	PizzaType() string
	PizzaIngredients() string
	BakingPizza() string
	CutingPizza() string
	GetPizzaInfo() string
}

func GetPizzaFactory(tipo string) (IPizzaFactory, error) {
	switch tipo {
	case "Hawaiana":
		return &HawaianaPizza{}, nil
	case "Peperonie":
		return &PeperoniPizza{}, nil
	default:
		return nil, errors.New("we do not sell this kind of pizza")
	}
}
