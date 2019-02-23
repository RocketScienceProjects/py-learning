def persons(**kwargs):
    kwargs = {
        'logGroupName': "log_group",
        'limit': 100,
        'logStreamNames': [
            'reasac-ava-uat-ECSStack-QRF69KUPN5BT/reasac-ava-int-svcs-consumers-accounting-events/adc56ecb-3785-4b86-a3f2-448bd5178afa',
        ],
    }
    print(kwargs)
    print(type(kwargs))



persons()