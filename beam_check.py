def beam_deflection():
    l = float(input(f"Beam Length (feet): "))
    h = float(input(f"Beam Depth (inches): "))
    b = float(input(f"Beam Width (inches): "))
    material = str(input(f"Material [S]teel or [C]oncrete or [W]ood: ")) or "S"
    building = str (input(f"Building Type [O]ffice, [R]esidential: ")) or "O"

    Av = round(b*h)
    S = round(1/6*b*h**2,2)
    I = round(1/12*b*h**3,2)
    E = 29000
    Fy = 60
    tribwidth = 10
    DL = 10
    LL = 50

    if building =="R":
        DL = 40
        LL = 20
    else:
        DL = 3.5/12*110
        LL = 50

    if material == "C":
        E = 3.6
        Fy = 4
        tribwidth = 10
    elif material == "W":
        E = 1.5
        Fy = 1410
        tribwidth = 1
    else:
        E = 29000

    psf = round(1.2*DL+1.6*LL,2)
    w = round(psf*tribwidth,2)
    M = int(round(w*l**2/8,0))
    V = int(round(w*l/2,0))
    Defl = round(5*w*(l*12)**4 / (384*E*1000*I),2)
    DeflAllowTotal = round(l/240,2)
    Mallow = int(round(0.66*Fy*1000*S/12,0))
    Vallow = int(round(0.5*Av*Fy*1000,0))

    bending = "NG"
    shear = "NG"
    deflection = "NG"

    if M <= Mallow:
        bending = "OK"
    else:
        bending = "NG"

    if V <= Vallow:
        shear = "OK"
    else:
        shear = "NG"
    
    if Defl <= DeflAllowTotal:
        deflection = "OK"
    else:
        deflection = "NG"


    summary = {
        "Deal Load": f"{DL} psf",
        "Live Load": f"{LL} psf",
        "Section Modulus": f"{S} in^3",
        "Moment Of Inertia": f"{I} in^4",
        "Elastic Modulus": f"{E} ksi",
        "Moment": f"{M} ft-lbs",
        "Allowable Moment": f"{Mallow} ft-lbs",
        "Bending Check": bending,
        "Shear": f"{V} lbs",
        "Allowable Shear": f"{Vallow} lbs",
        "Shear Check": shear,
        "Deflection": f"{Defl} in",
        "Allwoable Deflection": f"{DeflAllowTotal} in",
        "Deflection Check": deflection
    }

    keys = summary.keys()
    for k in keys:
        print(f"{k}: {summary[k]}\n")

beam_deflection()
    
