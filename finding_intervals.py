def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
	mergedCalendar = mergeCalendar(updatedCalendar1, updatedCalendar2)
	flattenedCalendar = flattenCalendar(mergedCalendar)
	return getaval(flattenedCalendar, meetingDuration)
	
def mergeCalendar(calendar1, calendar2):
	check = []
	i = 0
	j = 0
	while i < len(calendar1) and j < len(calendar2):
		a = timetominutes(calendar1[i][0])
		b = timetominutes(calendar2[j][0])
		if a < b:
			check.append(calendar1[i])
			i += 1
		else:
			check.append(calendar2[j])
			j += 1

	while i < len(calendar1):
		check.append(calendar1[i])
		i += 1
	while j < len(calendar2):
		check.append(calendar2[j])
		j += 1
	return check	

def updateCalendar(calendar, dailyBounds):
	updatedCalendar = calendar
	updatedCalendar.insert(0,["0:00",dailyBounds[0]])
	updatedCalendar.append([dailyBounds[1], "23:59"])
	return updatedCalendar

		
def flattenCalendar(check):
	flattened = [check[0]]
	for i in range(1,len(check)):
		current = check[i]
		prev = flattened[-1]
		a = timetominutes(prev[1])
		b = timetominutes(current[0])
		if a >= b:
			temp = [prev[0],minutestotime(max(a,timetominutes(current[1])))]
			flattened[-1] = temp
		else:
			flattened.append(current[:])
	return flattened

def getaval(flattened, meetingDuration):
	result = []
	diff = minutestotime(meetingDuration)
	for i in range(1,len(flattened)):
		a = timetominutes(flattened[i][0])
		b = timetominutes(flattened[i-1][1])
		if minutestotime(a - b) >= diff:
			result.append([flattened[i-1][1],flattened[i][0]])
	return result

def timetominutes(time):
	hours, mins = list(map(int,time.split(":")))
	return hours * 60 + mins

def minutestotime(minutes):
	hours = minutes // 60
	mins = minutes % 60
	hourstring = str(hours) if hours > 0 else "00"
	minsstring = "0" + str(mins) if mins < 10 else str(mins)
	return hourstring + ":" + minsstring
