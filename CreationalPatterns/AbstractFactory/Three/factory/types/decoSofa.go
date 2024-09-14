package types

type decoSofa struct {
	tipo string
	size string
	legs int8
}

func (s *decoSofa) GetType() string {
	return "Algo.. " + s.tipo
}

func (s *decoSofa) GetSize() string {
	return s.size
}

func (s *decoSofa) HasLegs() int8 {
	return s.legs
}
