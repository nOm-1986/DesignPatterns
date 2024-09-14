package factory

import (
	. "abstractfactory/factory/types"
	"errors"
	"fmt"
)

const (
	AdidasFactoryType string = "adidas"
	NikeFactoryType   string = "nike"
)

type ISportsFactory interface {
	MakeShoe(size int) IShoe
	MakeShirt(talla string) IShirt
}

func GetSportsFactory(factoryType string) (ISportsFactory, error) {
	switch factoryType {
	case AdidasFactoryType:
		return &Adidas{}, nil
	case NikeFactoryType:
		return &Nike{}, nil
	default:
		return nil, errors.New("unsuported notification type")
	}
}

func PrintShoeDetails(s IShoe) {
	fmt.Printf("Logo: %s", s.GetLogo())
	fmt.Println()
	fmt.Printf("Size: %d", s.GetSize())
	fmt.Println()
}

func PrintShirtDetails(s IShirt) {
	fmt.Printf("Logo: %s", s.GetLogo())
	fmt.Println()
	fmt.Printf("Size: %s", s.GetSize())
	fmt.Println()
}
