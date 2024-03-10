from datetime import datetime

import flet as ft
from flet import *
import requests

_current = requests.get("http://65.21.57.239/forecast").json()

def main(page: Page):
    page.title = 'Flet Counter App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_textbox = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def _current_temp():
        global _sunset, _sunrise
        # {"cloud_pct":20,"temp":11,"feels_like":10,"humidity":73,"min_temp":10,"max_temp":12,"wind_speed":7.2,"wind_degrees":260,
        # "sunrise":1706082974,"sunset":1706114241}
        _cloud_pct = _current['cloud_pct']
        _temp = _current['temp']
        _feels_like = _current['feels_like']
        _humidity = _current['humidity']
        _min_temp = _current['min_temp']
        _max_temp = _current['max_temp']
        _wind_speed = _current['wind_speed']
        _wind_degrees = _current['wind_degrees']
        _sunrise = _current['sunrise']
        _sunset = _current['sunset']

        return [_cloud_pct, _temp, _feels_like, _humidity, _min_temp, _max_temp, _wind_speed, _wind_degrees, _sunrise, _sunset,]

    def _current_extra():
        _extra_info = []
        _extra = [
            [
                datetime.fromtimestamp(_sunset).strftime("%I:%M %p"),
                "",
                "Sunset",
                f"sunset.png",
            ],
            [
                datetime.fromtimestamp(_sunrise).strftime("%I:%M %p"),
                "",
                "Sunrise",
                f"sunrise.png",
            ],
        ]

        for data in _extra:
            _extra_info.append(
                Container(
                    bgcolor="white10",
                    border_radius=12,
                    alignment=alignment.center,
                    content=Column(
                        alignment='center',
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                image_src=f"sunset.png",
                                width=32, height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment='center',
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        Text(str(data[0])+" "+data[1], size=14,),
                                        Text(data[2], size=11, color="white54",),
                                    ],
                                )
                            ),
                        ],
                    ),
                ),
            )

        return _extra_info

    def _top():
        _today = _current_temp()
        print(_today)
        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in _current_extra():
            _today_extra.controls.append(info)


        top = Container(width=310,
                        height=660 * 0.43,
                        gradient=LinearGradient(
                            begin=alignment.bottom_left,
                            end=alignment.top_right,
                            colors=["lightblue600", "lightblue900"],
                        ), border_radius=35,
                        animate=animation.Animation(duration=450, curve="decelerate"),
                        on_hover=lambda e: _expand(e),
                        padding=15,
                        content=Column(
                            alignment="start",
                            spacing=10,
                            controls=[
                                Row(
                                    alignment="center",
                                    controls=[Text(
                                        _current["City"].capitalize(),
                                        size=16,
                                        weight="w500",
                                        )]),
                                Row(
                                    spacing=5, alignment='spaceBetween', controls=[
                                        Row(expand=1, alignment='center', controls=[
                                            Container(
                                                content=Text(
                                                    _current['DOW']
                                                )
                                            )
                                        ])
                                    ]
                                ),
                                Container(padding=padding.only(bottom=5)),
                                Row(
                                    alignment="center",
                                    spacing=30,
                                    controls=[
                                        Column(
                                            controls=[
                                                Container(
                                                    width=90,
                                                    height=90,
                                                    image_src=f"cloud-computing.png",
                                                ),
                                            ]
                                        ),
                                        Column(
                                            spacing=5,
                                            horizontal_alignment='center',
                                            controls=[
                                                Text(
                                                    "Today",
                                                     size=12,
                                                     text_align="center",
                                                ),
                                                Row(
                                                    vertical_alignment='start',
                                                    spacing=0,
                                                    controls=[
                                                        Container(
                                                            content=Text(
                                                                _today[1],
                                                                size=52,
                                                            ),
                                                        ),
                                                        Container(
                                                            content=Text(
                                                                "º",
                                                                size=28,
                                                                text_align="center",
                                                            )
                                                        ),
                                                    ],
                                                ),
                                                # Text(
                                                #     str(_today[1]) + " - Overcast",
                                                #     size=10,
                                                #     color="white54",
                                                #     text_align="center",
                                                # ),
                                            ],
                                        ),
                            ],
                        ),
                        Divider(height=8, thickness=1, color="white10"),
                        Row(
                            alignment='spaceAround',
                            controls=[
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                         controls=[
                                            Container(
                                                alignment=alignment.center,
                                                image_src=f"wind.png",
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[6]) + " km/h",
                                                size=11,
                                            ),
                                            Text(
                                                "Wind",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    )
                                ),
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                image_src=f"humidity.png",
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[3]) + "%",
                                                size=11,
                                            ),
                                            Text(
                                                "Humidity",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    )
                                ),
                                Container(
                                    content=Column(
                                        horizontal_alignment="center",
                                        spacing=2,
                                        controls=[
                                            Container(
                                                alignment=alignment.center,
                                                image_src=f"thermometer.png",
                                                width=20,
                                                height=20,
                                            ),
                                            Text(
                                                str(_today[2]) + "º",
                                                size=11,
                                            ),
                                            Text(
                                                "Feels Like",
                                                size=9,
                                                color="white54",
                                            ),
                                        ],
                                    )
                                ),
                            ],
                        ),
                        _today_extra,
                    ],
                ),
            )

        return top

    # def _bot_data():
    #     _bot_data = []
    #
    #     _bot_data.append(
    #         Row(
    #             spacing=5, alignment='spaceBetween', controls=[
    #                 Row(expand=1, alignment='start', controls=[
    #                    Container(
    #                         alignment=alignment.center,
    #                         content=Text(
    #                             _current['DOW']
    #                         )
    #                    )
    #                 ])
    #             ]
    #         )
    #     )
    #
    #     return _bot_data

    def _bottom():
        _bot_column = Column(alignment="center", horizontal_alignment="center", spacing=25,)
        #
        # for data in _bot_data():
        #     _bot_column.controls.append(data)

        bottom = Container(padding=padding.only(top=280, left=20, right=20, bottom=20),
                           content=_bot_column,)

        return bottom

    _c = Container(
        width=310, height=550,
        border_radius=35, bgcolor="black",
        padding=10,
        content=Stack(width=300, height=550,
                      controls=[_bottom(), _top(),]),
    )

    def minus_click(e):
        if int(number_textbox.value) > 0:
            number_textbox.value = str(int(number_textbox.value) - 1)
            page.update()

    def plus_click(e):
        number_textbox.value = str(int(number_textbox.value) + 1)
        page.update()

    def _expand(e):
        if e.data == "true":
            _c.content.controls[1].height = 560
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.40
            _c.content.controls[1].update()

    page.add(_c)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
