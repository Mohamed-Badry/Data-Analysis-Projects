import time
import pandas as pd


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bike-share data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_prompt = "\nWould you like to view data for Chicago, New York City, or Washington? \n"

    city = input(city_prompt).lower()
    while city not in CITY_DATA.keys():
        print(f"{city} is not a valid city.")
        city = input(city_prompt).lower()

    # get user input for month (all, january, february, ... , june)
    month_prompt = "\nWhich month would you like to filter your data by? Jan, Feb, Mar, Apr, May, Jun, all \n"

    months = {'jan': 'january',
              'feb': 'february',
              'mar': 'march',
              'apr': 'april',
              'may': 'may',
              'jun': 'june',
              'all': 'all'}

    m_input = input(month_prompt).lower()
    month = months.get(m_input, m_input)

    while month not in months.values():
        print(f"{month} is not a valid month.")
        m_input = input(month_prompt).lower()
        month = months.get(m_input, m_input)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_prompt = "\nWhich day of the week would you like to sort by? Mon, Tue, Wed, Thu, Fri, Sat, Sun, or all \n"

    days = {'mon': 'monday',
            'tue': 'tuesday',
            'wed': 'wednesday',
            'thu': 'thursday',
            'fri': 'friday',
            'sat': 'saturday',
            'sun': 'sunday',
            'all': 'all'}

    d_input = input(day_prompt).lower()
    day = days.get(d_input, d_input)

    while day not in days.values():
        print(f"{day} is not a valid day")
        d_input = input(day_prompt).lower()
        day = days.get(d_input, d_input)

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print("Most common month:", months[most_common_month - 1].title())

    # display the most common day of week
    print("Most common day of week:", df['day_of_week'].mode()[0])

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour
    print("Most common start hour:", df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common start station:", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most common end station:", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trips'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    print("Most frequent trip:", df['Trips'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(
        f"Total travel time: {int(total_travel_time)} seconds or {total_travel_time / 3600:.2f} hours")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(
        f"Average travel time: {int(mean_travel_time)} seconds or {mean_travel_time / 60:.2f} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    # Displays statistics on bike-share users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types and counts: ")
    for user_type, count in user_types.items():
        print(f"{user_type}: {count}")

    if 'Gender' in df.columns:
        print("Genders counts: ")
        # Display counts of gender
        genders = df['Gender'].value_counts()
        for gender, count in genders.items():
            print(f"{gender}: {count}")

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth:", df['Birth Year'].min())
        print("Most recent year of birth:", df['Birth Year'].max())
        print("Most common year of birth:", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Asks the user if they want to see 5 rows of raw data until they say no"""
    n = 0
    restart = input(
        "\nDo you want to see 5 rows of raw data? yes / no\n").lower()
    while restart == 'yes':
        print(df.iloc[n:n + 5])
        n += 5
        restart = input(
            "\nDo you want to see the next 5 rows of raw data? yes / no\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
