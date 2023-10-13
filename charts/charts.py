import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    sizes = [215, 130, 245, 210]
    print("hi")

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.savefig('generated/pie_chart.png')
    plt.close()
