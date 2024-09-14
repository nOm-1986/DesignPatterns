package types

type ISofa interface {
	GetType() string
	GetSize() string
	HasLegs() int8
}
