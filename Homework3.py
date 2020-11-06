import numpy as np
import cmath
import matplotlib.pyplot as plt

# 1a  The semicircle is in x and z plane with z>0 so theta value is varied between -pi/2 to 0 to pi/2
a = 0.01
b = 1
r = np.sqrt(1e6)
frequencies = [300*1e6,3*1e9]
#
# print(c.imag)
# print(c.real)
# print(abs(c))


theta_range = np.linspace(-np.pi/2,np.pi/2,1000)
plot_row = 0
plot_column = 0

label = ['1(a) F=300MHz','2(a) F=3GHz']
color = ['r','b']
labelid = 0
for frequency in frequencies:
    lamda = (3 * 1e8) / frequency
    beta = (2 * np.pi) / lamda
    E_total = []
    # print(r)
    # print(lamda)
    # print(beta)
    c = complex((a * b * beta * np.sin(beta * r)) / (2 * np.pi * r),
                (a * b * beta * np.cos(beta * r)) / (2 * np.pi * r))

    for tetha in theta_range:
        E_theta = 0
        E_phi = (abs(c)/2)*(1+np.cos(tetha))

        E_total.append(20*np.log(np.sqrt(np.square(E_theta)+np.square(E_phi))))

    plt.plot(theta_range,E_total,color[labelid])
    plt.title(label[labelid])
    plt.xlabel(r'$\theta$')
    plt.ylabel('E_Total(dB)')
    plt.show()
    labelid+=1
#     plot_column+=1
# plot_row+=1
# plot_column=0

label = ['1(b) F=300MHz','2(b) F=3GHz']
labelid = 0
for frequency in frequencies:
    lamda = (3 * 1e8) / frequency
    beta = (2 * np.pi) / lamda
    E_total = []

    c = complex((a * b * beta * np.sin(beta * r)) / (2 * np.pi * r),
                (a * b * beta * np.cos(beta * r)) / (2 * np.pi * r))

    E_total =[]

    for theta in theta_range:
        E_phi = 0
        E_theta = ((abs(c)*lamda)/(2*np.pi*b*np.sin(theta)))*(1+np.cos(theta))*(np.sin((np.pi*b*np.sin(theta))/(lamda)))

        E_total.append(20*np.log(np.sqrt(np.square(E_theta)+np.square(E_phi))))
    plt.plot(theta_range, E_total, color[labelid])
    plt.title(label[labelid])
    plt.xlabel(r'$\theta$')
    plt.ylabel('E_Total(dB)')
    # plot_column += 1
    plt.show()
    labelid += 1

label = ['1(c) F=300MHz','2(c) F=3GHz']
labelid = 0
x = np.linspace(-100,100,100)
x = x*1e3
y = 0
z = 10*1e3
r = np.sqrt(np.square(x)+np.square(y)+np.square(z))
theta = np.arctan(y/x)
phi = np.arctan(np.sqrt((np.square(x)+np.square(y))/z))

print(x.shape)
print(r.shape)
print(theta.shape)
print(phi.shape)

plot_row += 1
plot_column = 0
for frequency in frequencies:
    lamda = (3 * 1e8) / frequency
    beta = (2 * np.pi) / lamda
    E_total = []
    c = [complex((a * b * beta * np.sin(beta * i)) / (2 * np.pi * i),(a * b * beta * np.cos(beta * i)) / (2 * np.pi * i)) for i in r]
    c = np.array(c)
    E_theta = 0

    E_phi = np.multiply((abs(c)/2),(1+np.cos(theta)))

    E_total = 20 * np.log(np.sqrt(np.square(E_theta) + np.square(E_phi)))
    print(E_total.shape)

    plt.plot(x/1000, E_total, color[labelid])
    plt.title(label[labelid])
    plt.xlabel('x(km)')
    plt.ylabel('E_Total(dB)')
    plt.show()
    labelid += 1


y = np.linspace(-100,100,100)
y = y*1e3
x = 0
z = 10*1e3
r = np.sqrt(np.square(x)+np.square(y)+np.square(z))
theta = np.arctan(y/x)
phi = np.arctan(np.sqrt((np.square(x)+np.square(y))/z))
label = ['1(d) F=300MHz','2(d) F=3GHz']
labelid = 0
plot_row +=1
plot_column = 0

for frequency in frequencies:
    lamda = (3 * 1e8) / frequency
    beta = (2 * np.pi) / lamda
    E_total = []
    c = [complex((a * b * beta * np.sin(beta * i)) / (2 * np.pi * i),(a * b * beta * np.cos(beta * i)) / (2 * np.pi * i)) for i in r]
    c = np.array(c)
    #
    E_phi = 0
    # print('c',c)
    # print('(1 + np.cos(theta))',(1 + np.cos(theta)))
    l = np.multiply((abs(c) * lamda),(1 + np.cos(theta)))
    # print('l',l)
    # E_theta = []
    # for i in range(len(y)):
    #     E_phi = 0
    #     E_theta.append(((abs(c[i]) * lamda) / (2 * np.pi * b * np.sin(theta[i]))) * (1 + np.cos(theta[i])) * (
    #         np.sin((np.pi * b * np.sin(theta[i])) / (lamda))))
    #

    m = np.multiply(l,np.sin((np.pi * b * np.sin(theta)) / (lamda)))
    # print(m.shape)
    n = 1./(2*np.pi*b*np.sin(theta))
    E_theta = np.multiply(m,n)

    E_total = 20 * np.log(np.sqrt(np.square(E_theta) + np.square(E_phi)))
    # # print(E_total.shape)
    print(E_total.shape)
    plt.plot(y/1000, E_total, color[labelid])
    plt.title(label[labelid])
    plt.xlabel('y(km)')
    plt.ylabel('E_Total(dB)')

    plt.show()
    labelid += 1



