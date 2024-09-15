package factory

import (
	"errors"
	"fmt"
	. "furniturefactory/factory/types"
)

const (
	ModernFactoryType    string = "moderna"
	ArtdecoFactoryType   string = "artdeco"
	VictorianFactoryType string = "victorian"
)

type IFurnitureFactory interface {
	MakeChair() IChair
	MakeSofa() ISofa
	MakeTable() ITable
}

func GetFurnitureFactory(factoryType string) (IFurnitureFactory, error) {
	switch factoryType {
	case ModernFactoryType:
		return &Modern{}, nil
	case ArtdecoFactoryType:
		return &Deco{}, nil
	case VictorianFactoryType:
		return &Victorian{}, nil
	default:
		return nil, errors.New("unsuported notification type")
	}
}

func PrintSofaDetails(s ISofa) {
	fmt.Printf("Sofa Information.... Type: %s. Size: %s. Legs: %d", s.GetType(), s.GetSize(), s.HasLegs())
	fmt.Println()
}

func PrintChairDetails(s IChair) {
	fmt.Printf("Chair Information.... Type: %s. Size: %s. Legs: %d", s.GetType(), s.GetSize(), s.HasLegs())
	fmt.Println()
}

func PrintTableDetails(s ITable) {
	fmt.Printf("Table Information.... Type: %s. Size: %s. Legs: %d", s.GetType(), s.GetSize(), s.HasLegs())
	fmt.Println()
}
