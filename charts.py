import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('agg')


def bar_chart(data):
    fig, ax = plt.subplots()
    ax.bar([r["university_location_code"] for r in data], [r["count"] for r in data])
    ax.set_xticks([r["university_location_code"] for r in data])
    ax.set_xlabel("University Location")
    ax.set_ylabel("Count")
    ax.set_title("University Rankings")
    return fig


def table(data):
    ranks = [d['position'] for d in data]
    universities = [d['university'] for d in data]
    fig, ax = plt.subplots()
    ax.set_axis_off()
    table_data = [[rank, university_name] for rank, university_name in zip(ranks, universities)]
    table = ax.table(cellText=table_data,
                     colLabels=['Rank', 'University Name'],
                     loc='center',
                     cellLoc="center",
                     colWidths=[0.09, 1.1],
                     colColours=["#9bc4e2"] * 2)
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 1.5)
    return fig
