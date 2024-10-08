# def bmi_calc_metric(weight,height) -> float:
#     return weight/(height **2)

def bmi_calc_imperial(weight,height) -> float:
    return (weight * 703)/(height**2)


def main() -> None:
    weight: float = 210 
    height: float = 73
    # bmi_metric: float = bmi_calc_metric(weight, height)
    bmi_imperial: float = bmi_calc_imperial(weight, height)
    print (f"Here is your BMI ${bmi_imperial: .2f}")
    
    
    
if __name__ == "__main__":
  main()