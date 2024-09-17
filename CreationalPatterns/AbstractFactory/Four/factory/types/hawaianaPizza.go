package types

type HawaianaPizza struct {
	ingredients []string
}

func (HawaianaPizza) PizzaType() string {
	return "🍕 Hawaiana 🍕"
}

func (h HawaianaPizza) PizzaIngredients() string {
	ingredientes := ""
	h.setIngredients()
	for _, v := range h.ingredients {
		ingredientes += " " + v + ","
	}
	return "Los ingredientes son: " + ingredientes
}

func (HawaianaPizza) BakingPizza() string {
	return "Horneada por 15 min a 300 grados centigrados"
}

func (HawaianaPizza) CutingPizza() string {
	return "Cortada en 8 porciones"
}

func (h HawaianaPizza) GetPizzaInfo() string {
	info := "Pizza " + h.PizzaType() + ".\n" + h.PizzaIngredients() + ".\n" + h.BakingPizza() + ".\n" + h.CutingPizza() + "."
	return info
}

func (h *HawaianaPizza) setIngredients() {
	h.ingredients = append(h.ingredients, "pizza dough", "tomato paste", "pinapple", "ham", "chese")
}
