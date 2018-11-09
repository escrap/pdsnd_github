import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print("-"*45)
print('Hello!If you want, let\'s explore some US bikeshare data!')
print("-"*45)

def get_city():

    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    while True:
        try:
            cities = ['chicago', 'new york city', 'washington']
            city=input("Enter a city. Choose among Chicago, New York City and Washington? ").lower()
            if city in cities :
                break
            else:
                print("Choose either Chicago, New York City or Washington. ")
        except:
                print("Ups! Something went wrong....")
    return city

def get_month():

    """
    Asks user to specify a month to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    while True:
        try:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month=input("Enter a month - january to june- you want to filter by. Type all to avoid filtering by month. ").lower()

            if month in months :
                break
            elif month =="all" :
                break
            else:
                print("Sorry but you only can't choose this option. ")

        except:
                print("Ups! Something went wrong.... ")
    return month

def get_day():

    """
    Asks user to specify a day to analyze.

    Returns:
        (str) day - name of the day of week to filter by, type "all" to apply no day filter.
    """
    while True:
        try:
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', ]
            day=input("Enter the name of the day of week  to filter by. Type all to avoid applying this filter. ").lower()
            if day in days :
                break
            elif day =="all" :
                break
            else:
                print("Sorry but you only can choose a dayoftheweek's name or the word all to avoid filtering. ")
        except:
                print("Ups! Something went wrong.")
    return day
    print('-'*50)
    print('-'*50)

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=get_city()
    # get user input for month (all, january, february, ... , june)
    month=get_month()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=get_day()

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
    df=pd.read_csv(CITY_DATA[city]) # Importing from a CSV file

    # Convert Start Time to Datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #Create a new column with a number from 1-12
    df['month']=df['Start Time'].dt.month
    #Create a new column with a number   from 0 to 6
    df['day_of_week']=df['Start Time'].dt.weekday_name

    if month !='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df

def time_stats(df,city):

    """Displays statistics."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month (both number and name)
    months=['january','february','march','april','may','june']
    most_common_month = df['month'].mode()[0]
    if most_common_month == 1:
        month_name=months[0].title()
        suffix='st'
    elif most_common_month == 2:
        month_name=months[1].title()
        suffix='nd'
    elif most_common_month == 3:
        month_name=months[2].title()
        suffix='rd'
    elif most_common_month == 4:
        month_name=months[3].title()
        suffix='th'
    elif most_common_month == 5:
        month_name=months[4].title()
        suffix='th'
    else:
        month_name=months[5].title()
        suffix='th'
    print()
    print("--Most common month : {}{} month. So, {}. ".format(most_common_month,suffix,month_name))


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print()
    print("--Most common day of week :", most_common_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print()
    print("--Most common start hour : {} h.".format(most_common_start_hour))
    print()
    print("In addition, we display an histogram ( frequencies vs. daytime among from 7h to 21h) of the bike usage under the filter parameters. \n \nIn case of Terminal display, close the pop-up window to let the program continue the execution. Thank you.")
    df[['hour']].plot(kind='hist',bins=[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],rwidth=0.9)
    plt.show()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df,city):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startStation = df['Start Station'].value_counts().idxmax()
    common_startStation_counts= df['Start Station'].value_counts()[0]
    print()
    print('--The most common start station in',' {} ' .format(city).title() ,'is:','\n--·',common_startStation , '(Count of: ' ,common_startStation_counts , 'times)')

    # display most commonly used end station
    common_endStation = df['End Station'].value_counts().idxmax()
    common_endStation_counts= df['End Station'].value_counts()[0]
    print()
    print('--The most common end station in',' {} ' .format(city).title() ,'is:','\n--·',common_endStation , '(Count of: ' ,common_endStation_counts , 'times)')

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] +' ---> '+ df['End Station']
    common_trip = df['trip'].value_counts().idxmax()
    common_trip_counts = df['trip'].value_counts()[0]
    print()
    print('--The most common trip in',' {} ' .format(city).title() ,'is:','\n--·', common_trip  ,'(Count of: ' ,common_trip_counts , 'times)')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df,city,month,day):

    """Displays statistics on the total and average trip duration."""
    start_time = time.time()
    print('\nCalculating Trip Duration...\n')

    # calculate statistics
    total_time =  df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()

    # show statistics
    print('--The total amount of travelling time in the city of','{}'.format(city).title(),' is:' , str(total_time), 'seconds.', '(Filtration done under criteria: Month =', month.title() , 'and Day =', day.title(),' )')
    print("--The average time of a trip is: " + str(mean_time),'seconds.')
    print()
    print()
    print('--Trip Duration statistics \n',df['Trip Duration'].describe())
    print()
    print("\nThis took %s seconds." % (time.time()-start_time))
    print('-'*40)

def user_stats(df,city):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender

    if city == 'chicago' :
        user_types_gender = df['Gender'].value_counts()
        print(user_types_gender)
        print()
    elif city == 'new york city':
        user_types_gender = df['Gender'].value_counts()
        print(user_types_gender)
        print()
    else:
        print()
        print("We don\'t have gender data for Washington and we can not show gender statistics")

    # Display earliest, most recent, and most common year of birth

    if city == 'chicago' :
        earliest_year_birth = df['Birth Year'].min()
        most_recent_year_birth= df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]

        print('--Most ancient year of birth: ', earliest_year_birth)
        print('--Most recent year of birth: ', most_recent_year_birth)
        print('--Most common birth year: ', common_year_birth)
        print()
    elif city == 'new york city':
        earliest_year_birth = df['Birth Year'].min()
        most_recent_year_birth= df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]

        print('--Oldest person to rent: ', earliest_year_birth)
        print('--Most recent year of birth: ', most_recent_year_birth)
        print('--Most common birth year: ', common_year_birth)
    else:
        print()
        print("--We don\'t have birth data for Washington and we can not show Year of Birth statistics")
        print()
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    """Displays data rows of bikeshare users in groups of five"""

    row_num = 0 #counter placed out of the 'if clause' to be able to go back to zero after every interaction with users.
    user_option = input("\n--Do you want to see the first 5 rows of data we have used? Any answer out of 'yes' will be considered as 'no'.  \n")
    while True:
        if user_option.lower() != 'yes':
            break
        if user_option.lower() == 'yes':
            df[row_num: row_num + 5] # prints FROM row_idx TO row_idx + 5
            print (df[row_num: row_num + 5])
            row_num = row_num + 5 # adds 5
            #time to update the variable (stays in yes? or changes?)
        user_option = input("\n--Would you like to see five more rows ? Any answer out of 'yes' will be considered as 'no'. \n")

def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,city)
        station_stats(df,city)
        trip_duration_stats(df,city,month,day)
        user_stats(df,city)

        display_data(df)


        restart = input("\n--Would you like to restart? Any answer out of 'yes' will be considered as 'no'.\n")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
