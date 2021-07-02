import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv', }
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days=['all','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Please choose a city from the following: Chicago, New York City or Washington (you could write the full city name or just the  first letter):\n").lower()
    if city=='w':
        city='washington'
    elif city=='n':
        city='new york city'
    elif city=='c':
        city='chicago'
    while city not in CITY_DATA:
        print("Please choose a valid city!")
        city=input("Please choose a city from the following: Chicago, New York City or Washington (you could write the full city name or just the  first letter):\n").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Please choose a month from January to June to filter by, or 'all' if you do not want a month filter: \n").lower()
    while month not in months:
        print("Please make sure that you wrote the correct month!")
        month=input("Please choose a month from January to June to filter by, or 'all' if you do not want a month filter: \n").lower()
    day=input("Please enter the day of your choice to filter by, or 'all' to apply no day filter: \n").lower()
    while day not in days:
        print("That is not a valid day!")
        day=input("Please enter the day of your choice to filter by, or 'all' to apply no day filter:\n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != months[0]:
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    month=months[common_month]
    print("The most common month for travelling is: {}\n".format(month.title()))
    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print("The most common day for travelling is: {}\n".format(common_day))
    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0]
    print("The most common hour for travelling is: {}\n".format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_count=df['Start Station'].value_counts()
    common_start=start_count.nlargest(1)
    print("The most commonly used start station by travellers is: {}\n".format(common_start))
    #print(df['Start Station'])
    # TO DO: display most commonly used end station
    end_count=df['End Station'].value_counts()
    common_end=end_count.nlargest(1)
    print("The most commonly used end station by travellers is: {}\n".format(common_end))


    # TO DO: display most frequent combination of start station and end station trip
    trip="Start: "+df['Start Station']+" End: "+df['End Station']
    trip=trip.value_counts()
    common_trip=trip.nlargest(1)
    print("The most common trip for travellers is: {}\n".format(common_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: {}\n".format(total_travel_time))
    # TO DO: display mean travel time

    avg_travel_time=df['Trip Duration'].mean()
    print("Average travel time is: {}\n".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    if city=='washington':
        print("There are no available user stats for {}".format(city.title()))
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print("Dsiplaying the counts of user types: \n")
        print(user_types)

        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("Dsiplaying the counts of each gender:\n")
        print(gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year=int(df['Birth Year'].min())
        recent_year=int(df['Birth Year'].max())
        common_year=int(df['Birth Year'].mode()[0])
        print("Displaying statistics on birth years of users:\n")
        print("Earliest year: {}\nRecent year: {}\nMost common year:{}".format(earliest_year,recent_year,common_year))
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """displays successive 5 rows from the raw data if requested by the user"""
    answer=input("Would you like to view raw data? (y or n)\n").lower()
    while answer!='y'and answer!='n':
        print("Oops! You have entered the wrong value! please type y or n")
        answer=input("Would you like to view raw data? (y or n)\n").lower()
    if answer=='y':
        i=0
        for i in range(i,len(df)):
            print(df.iloc[i,:])
            if (i+1)%5==0:
                answer=input("Would you like to view raw data? (y or n)\n")
                if answer=='n':
                    break
                elif answer=='y':
                    continue
                while answer!='y'and answer!='n':
                    print("Oops! You have entered the wrong value! please type y or n")
                    answer=input("Would you like to view raw data? (y or n)\n").lower()
    
def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            print("Displaying stats for {} while having '{}' as a month filter and '{}' as a day filter: \n".format(city.title(),month.title(),day.title()))
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            raw_data(df)
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyboardInterrupt as k :
            print("The program is shutting down")
            break
        except Exception as e:
            print("The following error occurred: {}".format(e))
            break
if __name__ == "__main__":
	main()
