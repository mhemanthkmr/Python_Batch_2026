from rich import print


def test(**kwargs):
    print(kwargs)
    print(kwargs.items())

    for i in kwargs.items():
        print(i[0], " === ", i[1])


test(
    name="Raj",
    start="Chennai",
    end="Malaysia",
    age="19",
    start_date="12-12-2025",
    end_date="16-12-2025",
    is_visa=True,
)
