res = []
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(13):
    d = datetime.datetime.now()-datetime.timedelta(days=i)
    if not d.weekday() in [4,5]:
        res.append(f'{WEEKDAYS[d.weekday()]} {d.day}/{d.month:02}/{d.year-2000}')
service_data = {'entity_id': 'input_select.tal_aviad', 'options': res}
hass.services.call('input_select', 'set_options', service_data)

