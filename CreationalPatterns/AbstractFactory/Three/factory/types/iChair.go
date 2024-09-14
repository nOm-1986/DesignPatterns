package types

type IChair interface {
	GetType() string
	GetSize() string
	HasLegs() int8
}
