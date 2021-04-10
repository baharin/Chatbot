# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
import sqlite3
from rasa_sdk.events import SlotSet

class BuildingNameSearch(Action):

	knowledge = []
	with open("individual-landmarks-1.csv", newline='\n') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='\t')
		for row in spamreader:
			knowledge.append(row)

	knowledge = knowledge[1:]

	def name(self) -> Text:

	     return "action_building_name_search"
	
	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		ans = ''
		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				ans = ''
				for i in range(len(self.knowledge)):
					c = False
					if name in self.knowledge[i][0]:
						dispatcher.utter_message(text="yes")
						ans = "yes"
						c = True
						break

				if c == False:

					dispatcher.utter_message(text="no")
					ans = "no"
					break


		return [SlotSet("answer", ans)]


class TellMeAbout(Action):

	def name(self) -> Text:
		return "action_tell_me_about"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		knowledge = []
		with open("individual-landmarks-1.csv", newline='\n') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				knowledge.append(row)

		knowledge = knowledge[1:]

		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				for i in range(len(knowledge)):
					knowledge[i] = knowledge[i][0].split("%")
					knowledge[i] = knowledge[i][1:]
				for i in range(len(knowledge)):

					c = False
					if name + "," == knowledge[i][0]:

						counter = 0
						address = knowledge[i][1]
						datebuilt = knowledge[i][2]
						architect = knowledge[i][3]
						dateoflandmark = knowledge[i][4]

						dispatcher.utter_message(text="Ok sure. Here is what I know: ")
						if len(address) != 0 and address != ",,":
							dispatcher.utter_message(text="The address is: " + address)
							counter = counter + 1

						if len(datebuilt) != 0 and datebuilt != ",,":
							dispatcher.utter_message(text="The built date is: " + datebuilt)
							counter = counter + 1

						if len(architect) != 0 and architect != ",,":
							dispatcher.utter_message(text="The architect(s): " + architect)
							counter = counter + 1

						if len(dateoflandmark) != 0 and dateoflandmark != ",,":
							dispatcher.utter_message(text="Date Designated a Chicago Landmark: " + dateoflandmark)
							counter = counter + 1

						if counter == 0:
							dispatcher.utter_message(text="Sorry! I couldn't find any information related to this landmark")

						c = True
						break

				if c == False:

					dispatcher.utter_message(text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

		return []


class BuiltDate(Action):

	def name(self) -> Text:
		return "action_built_date_of_building"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		knowledge = []
		with open("individual-landmarks-1.csv", newline='\n') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				knowledge.append(row)

		knowledge = knowledge[1:]

		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				for i in range(len(knowledge)):
					knowledge[i] = knowledge[i][0].split("%")
					knowledge[i] = knowledge[i][1:]
				for i in range(len(knowledge)):

					c = False

					if name + "," == knowledge[i][0]:

						date = knowledge[i][2]
						if len(date) != 0 and date != ",,":
							dispatcher.utter_message(text="This landmark was built in: "+ date)

							c = True
							break

						else:
							dispatcher.utter_message(text= "Sorry! I couldn't find the built date of this landmark.")
							c = True
							break

				if c == False:
					dispatcher.utter_message(
						text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

			if c == True:
				break
		return []

class Address(Action):

	def name(self) -> Text:
		return "action_address_of_building"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		knowledge = []
		with open("individual-landmarks-1.csv", newline='\n') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				knowledge.append(row)


		knowledge = knowledge[1:]

		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				for i in range(len(knowledge)):
					knowledge[i] = knowledge[i][0].split("%")
					knowledge[i] = knowledge[i][1:]
				for i in range(len(knowledge)):

					c = False

					if name + ',' == knowledge[i][0]:

						address = knowledge[i][1]
						if len(address) != 0 and address != ",,":
							dispatcher.utter_message(text="The address of this landmark is: " + address)

							c = True
							break

						else:
							dispatcher.utter_message(text="Sorry! I couldn't find the address of this landmark.")
							c = True
							break

				if c == False:

					dispatcher.utter_message(
						text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

		return []

class Architect(Action):

	def name(self) -> Text:
		return "action_architect_of_building"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		knowledge = []
		with open("individual-landmarks-1.csv", newline='\n') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				knowledge.append(row)

		knowledge = knowledge[1:]

		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				for i in range(len(knowledge)):
					knowledge[i] = knowledge[i][0].split("%")
					knowledge[i] = knowledge[i][1:]
				for i in range(len(knowledge)):

					c = False

					if name + "," == knowledge[i][0]:

						architect = knowledge[i][3]
						if len(architect) != 0 and architect != ",,":
							dispatcher.utter_message(text="The architect(s) of this landmark is (are): " + architect)

							c = True
							break

						else:
							dispatcher.utter_message(text="Sorry! I couldn't find the address of this landmark.")
							c = True
							break

				if c == False:
					dispatcher.utter_message(
						text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

		return []

class DesignatedDate(Action):

	def name(self) -> Text:
		return "action_designated_date_of_building"


	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		knowledge = []
		with open("individual-landmarks-1.csv", newline='\n') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='\t')
			for row in spamreader:
				knowledge.append(row)


		knowledge = knowledge[1:]

		for blob in tracker.latest_message['entities']:

			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False
				for i in range(len(knowledge)):
					knowledge[i] = knowledge[i][0].split("%")
					knowledge[i] = knowledge[i][1:]
				for i in range(len(knowledge)):

					c = False

					if name + "," == knowledge[i][0]:

						ddate = knowledge[i][4]
						if len(ddate) != 0 and ddate != ",,":
							dispatcher.utter_message(text="The designated date of this landmark is: " + ddate)

							c = True
							break

						else:
							dispatcher.utter_message(text="Sorry! I couldn't find the designated date of this landmark.")
							c = True
							break

				if c == False:
					dispatcher.utter_message(
						text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

		return []

class TellMeMore(Action):
	knowledge = []
	with open("individual-landmarks-1.csv", newline='\n') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='\t')
		for row in spamreader:
			knowledge.append(row)

	knowledge = knowledge[1:]

	for i in range(len(knowledge)):
		knowledge[i] = knowledge[i][0].split("%")
		knowledge[i] = knowledge[i][1:]

	def name(self) -> Text:
		return "action_Tell_me_more"


	def get_latest_intent(self, tracker: Tracker):

		events = tracker.events

		userevents = []
		for e in events:
			if e['event'] == 'user':
				userevents.append(e)


		intentnames = []
		for i in range(len(userevents)):
			intentnames.append(userevents[i]['parse_data']['intent']['name'])

		return intentnames


	def findbuildingname(self,tracker:Tracker):

		events = tracker.events

		userevents = []
		for e in events:
			if e['event'] == 'user':
				userevents.append(e)


		name = ''
		for i in range(len(userevents)-1,-1,-1):

			if len(userevents[i]['parse_data']['entities']) != 0 and userevents[i]['parse_data']['entities'][0]['entity'] =='building_name':
				name = userevents[i]['parse_data']['entities'][0]['value']
				break

		return name


	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		c = False
		for blob in tracker.latest_message['entities']:
			
			if blob['entity'] == 'building_name':
				name = blob['value']
				c = False

				for i in range(len(self.knowledge)):
					c = False

					if name + "," == self.knowledge[i][0]:

						intentnames = self.get_latest_intent(tracker)
						
						if intentnames[-2] == 'building_name_search':

							address = self.knowledge[i][1]
							datebuilt = self.knowledge[i][2]
							architect = self.knowledge[i][3]
							dateoflandmark = self.knowledge[i][4]

							counter = 0

							dispatcher.utter_message(text='Here is more: ')
							if len(address) != 0 and address != ",,":
								dispatcher.utter_message(text="The address is: " + address)
								counter = counter + 1

							if len(datebuilt) != 0 and datebuilt != ",,":
								dispatcher.utter_message(text="The built date is: " + datebuilt)
								counter = counter + 1

							if len(architect) != 0 and architect != ",,":
								dispatcher.utter_message(text="The architect(s): " + architect)
								counter = counter + 1

							if len(dateoflandmark) != 0 and dateoflandmark != ",,":
								dispatcher.utter_message(text="Date Designated a Chicago Landmark: " + dateoflandmark)
								counter = counter + 1

							if counter == 0:
								dispatcher.utter_message(
									text="Sorry! I couldn't find any information related to this landmark")

							c = True
							break

						else:
							a = []
							flag = False
							for j in range(len(intentnames)):

								if intentnames[j] == 'tell_me_about':
									dispatcher.utter_message(text="I told you everything I knew about this landmark. Sorry I can't find additional information about it.")
									c = True
									flag = True
									break

								elif intentnames[j] == 'built_date_of_building':
									a.append(2)
								elif intentnames[j] == 'address_of_building':
									a.append(1)
								elif intentnames[j] == 'architect_of_building':
									a.append(3)
								elif intentnames[j] == 'designated_date_of_building':
									a.append(4)
							if flag == True:
								break
							else:
								listt = [j for j in range(0,5)]
								a = list(list(set(listt)-set(a)) + list(set(a)-set(listt)))

								for j in range(len(a)):
									if a[j] == 1:
										if self.knowledge[i][1] != ",,":
											dispatcher.utter_message(text="The address is: " + self.knowledge[i][1])

									elif a[j] == 2:
										if self.knowledge[i][2] != ",,":
											dispatcher.utter_message(text="The built date is: " + self.knowledge[i][2])

									elif a[j] == 3:
										if self.knowledge[i][3] != ",,":
											dispatcher.utter_message(text="The archiect(s) is(are): " + self.knowledge[i][3])

									elif a[j] == 4:
										if self.knowledge[i][4] != ",,":
											dispatcher.utter_message(text="The Designated Date is: " + self.knowledge[i][4])

							c = True
							break

				if c == False:
					
					dispatcher.utter_message(
						text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")
					break

				return []

		name = self.findbuildingname(tracker)

		if name == '':
			dispatcher.utter_message(text= 'Sorry I don\'t know what landmark you are talking about.')

		else:
			for i in range(len(self.knowledge)):
				c = False

				if name + "," == self.knowledge[i][0]:

					intentnames = self.get_latest_intent(tracker)
					
					if intentnames[-2] == 'building_name_search':

						address = self.knowledge[i][1]
						datebuilt = self.knowledge[i][2]
						architect = self.knowledge[i][3]
						dateoflandmark = self.knowledge[i][4]

						counter = 0

						dispatcher.utter_message(text='Here is more: ')
						if len(address) != 0 and address != ",,":
							dispatcher.utter_message(text="The address is: " + address)
							counter = counter + 1

						if len(datebuilt) != 0 and datebuilt != ",,":
							dispatcher.utter_message(text="The built date is: " + datebuilt)
							counter = counter + 1

						if len(architect) != 0 and architect != ",,":
							dispatcher.utter_message(text="The architect(s): " + architect)
							counter = counter + 1

						if len(dateoflandmark) != 0 and dateoflandmark != ",,":
							dispatcher.utter_message(
								text="Date Designated a Chicago Landmark: " + dateoflandmark)
							counter = counter + 1

						if counter == 0:
							dispatcher.utter_message(
								text="Sorry! I couldn't find any information related to this landmark")

						c = True
						break

					else:
						a = []
						flag = False
						for j in range(len(intentnames)):

							if intentnames[j] == 'tell_me_about':
								dispatcher.utter_message(
									text="I told you everything I knew about this landmark. Sorry I can't find additional information about it.")
								c = True
								flag = True
								break

							elif intentnames[j] == 'built_date_of_building':
								a.append(2)
							elif intentnames[j] == 'address_of_building':
								a.append(1)
							elif intentnames[j] == 'architect_of_building':
								a.append(3)
							elif intentnames[j] == 'designated_date_of_building':
								a.append(4)
						if flag == True:
							break
						else:
							listt = [j for j in range(0, 5)]
							a = list(list(set(listt) - set(a)) + list(set(a) - set(listt)))

							for j in range(len(a)):
								if a[j] == 1:
									if self.knowledge[i][1] != ",,":
										dispatcher.utter_message(text="The address is: " + self.knowledge[i][1])

								elif a[j] == 2:
									if self.knowledge[i][2] != ",,":
										dispatcher.utter_message(
											text="The built date is: " + self.knowledge[i][2])

								elif a[j] == 3:
									if self.knowledge[i][3] != ",,":
										dispatcher.utter_message(
											text="The archiect(s) is(are): " + self.knowledge[i][3])

								elif a[j] == 4:
									if self.knowledge[i][4] != ",,":
										dispatcher.utter_message(
											text="The Designated Date is: " + self.knowledge[i][4])

						c = True
						break

			if c == False:
				
				dispatcher.utter_message(
					text="Sorry! It is not a landmark of Chicago. Please ask about landmarks in Chicago.")


		return []


class LandmarksBuiltByArchitect(Action):

	def name(self) -> Text:
		return "action_landmarks_architect_built"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for blob in tracker.latest_message['entities']:
			
			if blob['entity'] == 'architect_name':
				name = blob['value']
				
				connection = sqlite3.connect(":memory:")

				cursor = connection.cursor()

				sql_file = open("individual-landmarks-1.sql")

				sql_as_string = sql_file.read()

				cursor.executescript(sql_as_string)

				kkk = []
				for row in cursor.execute("SELECT name FROM individual_landmarks_1 WHERE architect LIKE " + '\'' + "%" + name + "%" + '\''):

					
					kkk.append(row)

				
				if len(kkk) > 0:

					dispatcher.utter_message(text="Here you are! The landmark(s) that the architect built are: ")
					for k in range(len(kkk)):
						#c = list(kkk[0])
						
						c = kkk[k][0]
						dispatcher.utter_message(text="" + c)

				else:
					dispatcher.utter_message(text="Sorry! I can't find any landmarks that this architect built. Please ask about another architect.")

				break

		return []


class LandmarksAfterDate(Action):

	def name(self) -> Text:
		return "action_landmarks_after_dates"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		for blob in tracker.latest_message['entities']:
			
			if blob['entity'] == 'date':
				name = blob['value']
				name = name[:4]
				
				#name = int(name)
				connection = sqlite3.connect(":memory:")

				cursor = connection.cursor()

				sql_file = open("individual-landmarks-1.sql")

				sql_as_string = sql_file.read()

				cursor.executescript(sql_as_string)

				kkk = []
				for row in cursor.execute("SELECT name,built FROM individual_landmarks_1 WHERE built <> '' AND built > " + name ):
					
				if len(kkk) > 0:

					dispatcher.utter_message(text="Here you are! The landmark(s) built after this date is(are): ")
					for k in range(len(kkk)):
						# c = list(kkk[0])
						
						c = kkk[k][0]
						dispatcher.utter_message(text="" + c)

				else:
					dispatcher.utter_message(
						text="Sorry! I can't find any landmarks built after this date. Please ask about another date.")

				break

		return []


class LandmarksBetweenDate(Action):

	def name(self) -> Text:
		return "action_landmarks_between_dates"

	def extractdates(self,tracker: Tracker):

		dates = []
		for blob in tracker.latest_message['entities']:
			if blob['entity'] == 'date' or blob['entity'] == 'date2':
				dates.append(blob['value'])

		return dates


	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		date = self.extractdates(tracker)
		
		date1 = date[0]
		date2 = date[1]
		connection = sqlite3.connect(":memory:")

		cursor = connection.cursor()

		sql_file = open("individual-landmarks-1.sql")

		sql_as_string = sql_file.read()

		cursor.executescript(sql_as_string)

		kkk = []
		for row in cursor.execute("SELECT name,built FROM individual_landmarks_1 WHERE built <> '' AND built >= " + date1 + " AND built <= " + date2):
			
			kkk.append(row)

				if len(kkk) > 0:

			dispatcher.utter_message(text="Here you are! The landmark(s) built between " + date1 + "and " + date2)
			for k in range(len(kkk)):
				# c = list(kkk[0])
				
				c = kkk[k][0]
				dispatcher.utter_message(text="" + c)

		else:
			dispatcher.utter_message(
				text="Sorry! I can't find any landmarks built between these dates. Please ask about another dates.")


		return []

class ResetSlot(Action):

	def name(self) -> Text:
		return "reset_slot"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		return [SlotSet("answer", None)]
