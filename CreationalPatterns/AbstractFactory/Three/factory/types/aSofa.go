package types

type Sofa struct {
	tipo string
	size string
	legs int8
}

func (s *Sofa) GetType() string {
	return s.tipo
}

func (s *Sofa) GetSize() string {
	return s.size
}

func (s *Sofa) HasLegs() int8 {
	return s.legs
}
