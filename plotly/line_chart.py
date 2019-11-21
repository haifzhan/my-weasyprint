import plotly.graph_objects as pgo
import plotly.io as pio

primary_color = '#14213d'
secondary_color = '#1fe494'

title_font = dict(color=secondary_color, size=24, )
axis_title_font = dict(color=secondary_color, size=18)


class LineChart:

    @staticmethod
    def build_chart(output):
        data = [1, 18, 21, 10, 17, 5, 3]
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        layout = LineChart.build_layout()
        fig = pgo.Figure(layout=layout)
        fig.add_trace(pgo.Scatter(
            x=days,
            y=data,
            line=dict(color='#ffffff',),
        ))

        pio.write_image(fig, output)

    @staticmethod
    def build_layout():
        title = '<b>' + 'Weekdays Commits in March' + '</b>'
        legend_settings = dict(traceorder='normal', font=dict(color=secondary_color, size=16))
        return pgo.Layout(
            paper_bgcolor=primary_color,
            plot_bgcolor=primary_color,
            title=dict(text=title, pad=dict(t=-5, l=-5, r=-5, ), font=title_font),
            showlegend=True,
            legend=legend_settings,
            xaxis=LineChart._axis('Weekdays', range=None),
            yaxis=LineChart._axis('Commits', range=None),
        )

    @staticmethod
    def _axis(axis_name, range):
        return dict(
            gridcolor='#366c70',
            zerolinecolor='#366c70',
            showgrid=True,
            zeroline=True,
            title=axis_name,
            titlefont=axis_title_font,
            color='#9ebfc3',
            tickfont=dict(size=18),
            range=range
        )


if __name__ == '__main__':
    LineChart.build_chart('/Users/hzhang/Lab/python-projects/my-weasyprint/assets/line_chart.svg')
