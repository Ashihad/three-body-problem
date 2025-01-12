from .Utils import *

def sun_earth_mars():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)  # earth
  params['3'] = ObjectParams2D(0, 2.28e11, 24.07e3, 0, 6.42e23) # mars
  params['days'] = 365
  params['frames'] = 500
  params['title'] = "Sun-Earth-Mars system"
  return params

def newton_problem():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)                            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)                  # earth
  params['3'] = ObjectParams2D(0, 1.5e11+384_400_000, 29.78e3+1022, 0, 7.35e22) # moon
  params['days'] = 31
  params['frames'] = 500
  params['title'] = "Newton problem (Sun-Earth-Moon system)"
  return params

def triangle():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, 0, 0, 1.989e32)
  params['3'] = ObjectParams2D(0, 1*1.5e11, 0, 0, 1.989e32)
  params['days'] = 365
  params['frames'] = 500
  params['title'] = "Equilateral triangle configuration"
  return params

def rotating_triangle():
  # does not work
  params = {}
  # params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -500, 500*np.sqrt(3), 1.989e32)
  # params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -500*np.sqrt(3), -500, 1.989e32)
  # params['3'] = ObjectParams2D(0, 1*1.5e11, 1000, 0, 1.989e32)
  params['G'] = 6.67430e-11
  v1 = np.sqrt(6.67430e-11 * 3*1.989e32 / 1*1.5e11)/1000
  params['1'] = ObjectParams2D(-np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -1/2*v1, v1*np.sqrt(3), 1.989e32)
  params['2'] = ObjectParams2D( np.sqrt(3)/2*1.5e11, -1/2*1.5e11, -v1*np.sqrt(3), -1/2*v1, 1.989e32)
  params['3'] = ObjectParams2D(0, 1*1.5e11, v1, 0, 1.989e32)
  params['days'] = 365
  params['frames'] = 500
  return params

def burrau():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 5)
  params['2'] = ObjectParams2D(-3, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem"
  return params

def burrau_shifted():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0.000001, -0.000001, 0, 0, 5)
  params['2'] = ObjectParams2D(-3.000001, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4.000001, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem, shifted by 1e-6"
  return params

def burrau_less_shifted():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0.000000000001, -0.000000000001, 0, 0, 5)
  params['2'] = ObjectParams2D(-3.000000000001, 0, 0, 0, 4)
  params['3'] = ObjectParams2D(0, 4.000000000001, 0, 0, 3)
  params['days'] = 80
  params['frames'] = 500
  params['title'] = "Burrau problem, shifted by 1e-12"
  return params

# https://arxiv.org/pdf/1705.00527

def xiaoming_li_et_all_1():
  # December 2017
  params = {}
  params['G'] = 1
  v1 = 0.4159559963
  v2 = 0.2988672319
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 500
  params['title'] = "Xiaoming Li et al"
  return params

def xiaoming_li_et_all_2():
  # December 2017
  params = {}
  params['G'] = 1
  v1 = 0.3231926176
  v2 = 0.3279135713
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 1000
  params['title'] = "Xiaoming Li et al"
  return params

def xiaoming_li_et_all_3():
  # December 2017
  params = {}
  params['G'] = 1
  v1 = 0.3369172422
  v2 = 0.2901238678
  params['1'] = ObjectParams2D(-1, 0, v1, v2, 1)
  params['2'] = ObjectParams2D(1, 0, v1, v2, 1)
  params['3'] = ObjectParams2D(0, 0, -2*v1, -2*v2, 1)
  params['days'] = 1/24/60*2  # 2 minutes
  params['frames'] = 1000
  params['title'] = "Xiaoming Li et al"
  return params

def l1():
  params = {}
  params['G'] = 6.67430e-11
  params['1'] = ObjectParams2D(0, 0, 0, 0, 1.989e30)                            # sun
  params['2'] = ObjectParams2D(0, 1.5e11, 29.78e3, 0, 5.97e24)                  # earth
  params['3'] = ObjectParams2D(
    0, 
    1.5e11 - (1.5e11*((5.97e24/(5.97e24+1.989e30))/3)**(1/3)), 
    29.78e3, 
    0, 
    1e3
  )                    # satellite
  params['days'] = 365*2
  params['frames'] = 500
  params['title'] = "L1 Lagrange point (Sun-Earth-satellite system)"
  return params

def butterfly():
  # Suvakov et all
  # https://d1wqtxts1xzle7.cloudfront.net/35314308/PhysRevLett.110.114301-libre.pdf?1414532854=&response-content-disposition=inline%3B+filename%3DThree_Classes_of_Newtonian_Three_Body_Pl.pdf&Expires=1736637888&Signature=BgW9VEbj3h~LWtuJrAIY668dqaAEfmOBdN3HEMwa8lNN3O1OuoMMT0ckTebycVysRI6CZFML-8w~m8ilCH56MoKzU16rtac3EwFLKhc4u2Q2slc2CQ91-cxzlivugyPZwFlQ7teF6yI~xTnpah1QVQw7xaaYviMtNT0VISrmvkiN6rnub1rkw~KcWzM2undzMwdZ7EV7DmbzNOqzDI2Q68wGJVE2Cofj9R7g1-6-oRKfIZf~-QE3fRN9xwjz1jI~2VN7AoyQCWxSdmP8g6Ww8qWNTpCnOMWX7mYYroNeIGaplsNms5KndLI8LEpk1czsNo3jrLTRRummynCESgbSSA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
  params = {}
  params['G'] = 1
  vx = 0.30689
  vy = 0.12551
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*12 # 12 seconds
  params['frames'] = 500
  params['title'] = "\"Butterfly\" configuration"
  return params

def bumblebee():
  # Suvakov et all
  # https://d1wqtxts1xzle7.cloudfront.net/35314308/PhysRevLett.110.114301-libre.pdf?1414532854=&response-content-disposition=inline%3B+filename%3DThree_Classes_of_Newtonian_Three_Body_Pl.pdf&Expires=1736637888&Signature=BgW9VEbj3h~LWtuJrAIY668dqaAEfmOBdN3HEMwa8lNN3O1OuoMMT0ckTebycVysRI6CZFML-8w~m8ilCH56MoKzU16rtac3EwFLKhc4u2Q2slc2CQ91-cxzlivugyPZwFlQ7teF6yI~xTnpah1QVQw7xaaYviMtNT0VISrmvkiN6rnub1rkw~KcWzM2undzMwdZ7EV7DmbzNOqzDI2Q68wGJVE2Cofj9R7g1-6-oRKfIZf~-QE3fRN9xwjz1jI~2VN7AoyQCWxSdmP8g6Ww8qWNTpCnOMWX7mYYroNeIGaplsNms5KndLI8LEpk1czsNo3jrLTRRummynCESgbSSA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
  params = {}
  params['G'] = 1
  vx = 0.18428
  vy = 0.58719
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*70 # 70 seconds
  params['frames'] = 500
  params['title'] = "\"Bumblebee\" configuration"
  return params

def goggles():
  # Suvakov et all
  # https://d1wqtxts1xzle7.cloudfront.net/35314308/PhysRevLett.110.114301-libre.pdf?1414532854=&response-content-disposition=inline%3B+filename%3DThree_Classes_of_Newtonian_Three_Body_Pl.pdf&Expires=1736637888&Signature=BgW9VEbj3h~LWtuJrAIY668dqaAEfmOBdN3HEMwa8lNN3O1OuoMMT0ckTebycVysRI6CZFML-8w~m8ilCH56MoKzU16rtac3EwFLKhc4u2Q2slc2CQ91-cxzlivugyPZwFlQ7teF6yI~xTnpah1QVQw7xaaYviMtNT0VISrmvkiN6rnub1rkw~KcWzM2undzMwdZ7EV7DmbzNOqzDI2Q68wGJVE2Cofj9R7g1-6-oRKfIZf~-QE3fRN9xwjz1jI~2VN7AoyQCWxSdmP8g6Ww8qWNTpCnOMWX7mYYroNeIGaplsNms5KndLI8LEpk1czsNo3jrLTRRummynCESgbSSA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
  params = {}
  params['G'] = 1
  vx = 0.08330
  vy = 0.12789
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*20 # 20 seconds
  params['frames'] = 500
  params['title'] = "\"Goggles\" configuration"
  return params

def yinyang():
  # Suvakov et all
  # https://d1wqtxts1xzle7.cloudfront.net/35314308/PhysRevLett.110.114301-libre.pdf?1414532854=&response-content-disposition=inline%3B+filename%3DThree_Classes_of_Newtonian_Three_Body_Pl.pdf&Expires=1736637888&Signature=BgW9VEbj3h~LWtuJrAIY668dqaAEfmOBdN3HEMwa8lNN3O1OuoMMT0ckTebycVysRI6CZFML-8w~m8ilCH56MoKzU16rtac3EwFLKhc4u2Q2slc2CQ91-cxzlivugyPZwFlQ7teF6yI~xTnpah1QVQw7xaaYviMtNT0VISrmvkiN6rnub1rkw~KcWzM2undzMwdZ7EV7DmbzNOqzDI2Q68wGJVE2Cofj9R7g1-6-oRKfIZf~-QE3fRN9xwjz1jI~2VN7AoyQCWxSdmP8g6Ww8qWNTpCnOMWX7mYYroNeIGaplsNms5KndLI8LEpk1czsNo3jrLTRRummynCESgbSSA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
  params = {}
  params['G'] = 1
  vx = 0.51394
  vy = 0.30474
  params['1'] = ObjectParams2D(-1, 0, vx, vy, 1)
  params['2'] = ObjectParams2D(1, 0, vx, vy, 1)
  params['3'] = ObjectParams2D(0, 0, -2*vx, -2*vy, 1)
  params['days'] = 1/24/60/60*35 # 35 seconds
  params['frames'] = 500
  params['title'] = "\"Yin Yang\" configuration"
  return params
