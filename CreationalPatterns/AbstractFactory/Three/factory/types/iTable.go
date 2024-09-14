package types

type ITable interface {
	GetType() string
	GetSize() string
	HasLegs() int8
}
