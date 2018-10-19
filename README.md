# ChasesList
Nationwide Craitslist Vehicle Search App built with Python

To start, update the file config.conf with your desired locations and query_strings.

Example of configuration file:

```python
	locations = ["lincoln", "nebraska"] # see below for list of all national locations
	query_strings = ["query=toyota+pickup"] # see below for more detailed example query_strings and url string values
```

Now start the main python script simple using:

```python
	python3 scraper.py
```

The output is a simple html file with the posts found. The html ouput file is named with the datetime of when the script was run.

You'll need to use BeautifulSoup and python3, see requirements.txt for details.


```python
	query_strings = ["query=toyota"]

	add additional url string arguments for more detailed searches:
	    ex:
	        "query=toyota+hatchback"
	    ex:
	        "query=toyota+truck&bundleDuplicates=1&max_auto_year=1994&"


	url string arguments MUST follow `...org/search/cto?["query_string"]`

        - mass search arguments -
            bundle duplicate postings = &bundleDuplicates=1
            only posts posted TODAY = &postedToday=1
            only posts WITH titles = &srchType=T
            only posts WITH photos = &hasPic=1

	    - year -
	        minimum auto year = &min_auto_year=2017
	        maximum auto year = &max_auto_year=2018

	    - odometer/miles -
	        minimum number of miles = &min_auto_miles=1000
	        maximum number of miles = &max_auto_miles=300000

	    - drive -
            front wheel drive = &auto_drivetrain=1
            rear wheel drive = &auto_drivetrain=2
            four wheel drive = &auto_drivetrain=3

	    - transmission -
            manual transmission = &auto_transmission=1
            automatic transmission = &auto_transmission=2
            other transmission = &auto_transmission=3

	    - fuel type -
            gasoline/petrol = &auto_fuel_type=1
            diesel = &auto_fuel_type=2
            hybrid = &auto_fuel_type=3
            electric = &auto_fuel_type=4
            other = &auto_fuel_type=5

        - number of cylinders -
            3cyl = &auto_cylinders=1
            4cyl = &auto_cylinders=2
            5cyl = &auto_cylinders=3
            6cyl = &auto_cylinders=4
            8cyl = &auto_cylinders=5
            10cyl = &auto_cylinders=6
            12cyl = &auto_cylinders=7
            other = &auto_cylinders=8

        - condition -
            new = &condition=10
            like new = &condition=20
            excellent = &condition=30
            good = &condition=40
            fair = &condition=50
            salvage = &condition=60

	    - title status -
            clean title = &auto_title_status=1
            salvage title = &auto_title_status=2
            rebuilt title = &auto_title_status=3
            parts only = &auto_title_status=4
            lien title = &auto_title_status=5
            missing title = &auto_title_status=6

```

```python

    Full list of craigslist locales to pass into your `locales=["cityName"]` config
        query_strings = ["query=toyota&bundleDuplicates=1&max_auto_year=1994&auto_drivetrain=3"]

["lincoln", "omaha",  "grandisland", "northplatte", "auburn", "bham", "dothan",
"shoals", "gadsden", "huntsville", "mobile", "montgomery", "tuscaloosa", "anchorage", "fairbanks",
"kenai", "juneau", "flagstaff", "mohave", "phoenix", "prescott", "showlow", "sierravista", "tucson",
"yuma", "fayar", "fortsmith", "jonesboro", "littlerock", "texarkana", "bakersfield", "chico", "fresno",
"goldcountry", "hanford", "humboldt", "imperial", "inlandempire", "losangeles", "mendocino", "merced",
"modesto", "monterey", "orangecounty", "palmsprings", "redding", "sacramento", "sandiego", "sfbay", "slo",
"santabarbara", "santamaria", "siskiyou", "stockton", "susanville", "ventura", "visalia", "yubasutter",
"boulder", "cosprings", "denver", "eastco", "fortcollins", "rockies", "pueblo", "westslope", "newlondon",
"hartford", "newhaven", "nwct", "delaware", "washingtondc", "miami", "daytona", "keys", "fortlauderdale",
"fortmyers", "gainesville", "cfl", "jacksonville", "lakeland", "miami", "lakecity", "ocala", "okaloosa",
"orlando", "panamacity", "pensacola", "sarasota", "miami", "spacecoast", "staugustine", "tallahassee",
"tampa", "treasure", "miami", "albanyga", "athensga", "atlanta", "augusta", "brunswick", "columbusga",
"macon", "nwga", "savannah", "statesboro", "valdosta", "honolulu", "boise", "eastidaho", "lewiston",
"twinfalls", "bn", "chambana", "chicago", "decatur", "lasalle", "mattoon", "peoria", "rockford", "carbondale",
"springfieldil", "quincy", "bloomington", "evansville", "fortwayne", "indianapolis", "kokomo", "tippecanoe",
"muncie", "richmondin", "southbend", "terrehaute", "ames", "cedarrapids", "desmoines", "dubuque", "fortdodge",
"iowacity", "masoncity", "quadcities", "siouxcity", "ottumwa", "waterloo", "lawrence", "ksu", "nwks",
"salina", "seks", "swks", "topeka", "wichita", "bgky", "eastky", "lexington", "louisville", "owensboro",
"westky", "batonrouge", "cenla", "houma", "lafayette", "lakecharles", "monroe", "neworleans", "shreveport",
"maine", "annapolis", "baltimore", "easternshore", "frederick", "smd", "westmd", "boston", "capecod",
"southcoast", "westernmass", "worcester", "annarbor", "battlecreek", "centralmich", "detroit", "flint",
"grandrapids", "holland", "jxn", "kalamazoo", "lansing", "monroemi", "muskegon", "nmi", "porthuron",
"saginaw", "swmi", "thumb", "up", "bemidji", "brainerd", "duluth", "mankato", "minneapolis", "rmn",
"marshall", "stcloud", "gulfport", "hattiesburg", "jackson", "meridian", "northmiss", "natchez",
"columbiamo", "joplin", "kansascity", "kirksville", "loz", "semo", "springfield", "stjoseph",
"stlouis", "billings", "bozeman", "butte", "greatfalls", "helena", "kalispell", "missoula", "montana",
"scottsbluff", "elko", "lasvegas", "reno", "nh", "cnj", "jerseyshore", "newjersey", "southjersey",
"albuquerque", "clovis", "farmington", "lascruces", "roswell", "santafe", "albany", "binghamton", "catskills",
"chautauqua", "elmira", "fingerlakes", "glensfalls", "hudsonvalley", "ithaca",
"longisland", "newyork", "oneonta", "plattsburgh", "syracuse", "twintiers",
"utica", "asheville", "boone", "charlotte", "eastnc", "fayetteville", "greensboro",
"hickory", "onslow", "outerbanks", "raleigh", "wilmington", "winstonsalem", "bismarck", "fargo",
"grandforks", "nd", "akroncanton", "ashtabula", "athensohio", "chillicothe", "cincinnati", "cleveland",
"columbus", "dayton", "limaohio", "mansfield", "sandusky", "toledo", "tuscarawas", "youngstown", "zanesville",
"lawton", "enid", "oklahomacity", "stillwater", "tulsa", "bend", "corvallis", "eastoregon", "eugene", "klamath",
"medford", "oregoncoast", "portland", "roseburg", "salem", "altoona", "chambersburg", "erie", "harrisburg",
"lancaster", "allentown", "meadville", "philadelphia", "pittsburgh", "poconos", "reading", "scranton",
"pennstate", "williamsport", "york", "providence", "charleston", "columbia", "florencesc", "greenville",
"hiltonhead", "myrtlebeach", "nesd", "csd", "rapidcity", "siouxfalls", "sd", "chattanooga", "clarksville",
"cookeville", "jacksontn", "knoxville", "memphis", "nashville", "tricities", "abilene", "amarillo", "austin",
"beaumont", "brownsville", "collegestation", "corpuschristi", "dallas", "nacogdoches", "delrio", "elpaso",
"galveston", "houston", "killeen", "laredo", "lubbock", "mcallen", "odessa", "sanangelo", "sanantonio",
"sanmarcos", "bigbend", "texoma", "easttexas", "victoriatx", "waco", "wichitafalls", "logan", "ogden", "provo",
"saltlakecity", "stgeorge", "burlington", "charlottesville", "danville", "fredericksburg", "norfolk", "harrisonburg",
"lynchburg", "blacksburg", "richmond", "roanoke", "swva", "winchester", "kpr", "moseslake",
"pullman", "seattle", "spokane", "wenatchee", "yakima", "charlestonwv", "martinsburg", "huntington",
"morgantown", "wheeling", "parkersburg", "swv", "wv", "appleton", "eauclaire", "greenbay", "janesville", "racine",
"lacrosse", "madison", "milwaukee", "northernwi", "sheboygan", "wausau", "wyoming"]
