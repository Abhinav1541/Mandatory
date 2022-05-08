
def get_super(input):
    ''' This function will change the input string into a superscript string'''
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    '''The maketrans() method returns a mapping table that can be used with the
     translate() method to replace specified characters.'''
    res = input.maketrans(''.join(normal), ''.join(super_s))
    return input.translate(res)


def get_sub(input):
    ''' This function will change the input string into a subscript string'''
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = input.maketrans(''.join(normal), ''.join(sub_s))
    return input.translate(res)

class introduction:
  ''' To demonstrate my python programming skills, I set up a python class to
   give a brief introduction about myself '''
  def __init__(self, name, age, college, department, year_of_study, interests):
    ''' The __init__ method is used to initialize the object’s state (constructor)'''
    self.name = name
    self.age = age
    self.college = college
    self.department = department
    self.year_of_study = year_of_study
    self.interests = interests


  def my_intro(self):
    ''' The my_intro method will use all the variables defined in the
     introduction class to give a brief introduction about myself '''
    print("Hello everyone, my name is", self.name, "and I am", self.age, "years old.")
    print("I am a", self.year_of_study, "nd year", self.department ,"undergraduate at", self.college)
    print("My interests are:", interests_abhinav)

interests_abhinav = {
  "Sport": "Cricket",
  "IPL_team": "Mumbai Indians",
  "Coding_Language": "Python",
  "Electrical_core": "Nothing"
}

Myself = introduction("Abhinav Singh", 21, "SRM Institute of Science and Technology, Chennai", "Electrical", 2, interests_abhinav)

Myself.my_intro()