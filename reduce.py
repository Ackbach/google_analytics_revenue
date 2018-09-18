import os

# We are going to reduce the file size by replacing
# the idiotic string ""not available in demo dataset""
# by "n/a". This should reduce the dataset enormously,
# and will help us have an idea of null values in
# the data.

# First we play with head.csv, so we don't damage the
# entire dataset.


base_path = '/home/akeister/Data/Google Analytics Revenue/'
read_file = os.path.join(base_path, 'train.csv')
write_file = os.path.join(base_path, 'train_reduced.csv')

with open(read_file, 'r') as input_file:
    with open(write_file, 'w') as output_file:
        for line in input_file:
            line = line.replace("""\"not available in demo dataset\"""", "\"n/a\"")
            line = line.replace("""\"browser\"""", "\"brws\"")
            line = line.replace("""\"Internet Explorer\"""", "\"IE\"")
            line = line.replace("""\"browserVersion\"""", "\"brwsVer\"")
            line = line.replace("""\"browserSize\"""", "\"brwsSize\"")
            line = line.replace("""\"operatingSystem\"""", "\"OS\"")
            line = line.replace("""\"Macintosh\"""", "\"Mac\"")
            line = line.replace("""\"Windows\"""", "\"Win\"")
            line = line.replace("""\"Linux\"""", "\"Lnx\"")
            line = line.replace("""\"operatingSystemVersion\"""", "\"OSVer\"")
            line = line.replace("""\"isMobile\"""", "\"isMbl\"")
            line = line.replace("""\"mobileDeviceBranding\"""", "\"mblDevBrnd\"")
            line = line.replace("""\"mobileDeviceModel\"""", "\"blDevMdl\"")
            line = line.replace("""\"mobileInputSelector\"""", "\"mblInSlct\"")
            line = line.replace("""\"mobileDeviceInfo\"""", "\"mblDevInfo\"")
            line = line.replace("""\"mobileDeviceMarketingName\"""", "\"mblDevMrktName\"")
            line = line.replace("""\"flashVersion\"""", "\"flshVer\"")
            line = line.replace("""\"language\"""", "\"lang\"")
            line = line.replace("""\"screenColors\"""", "\"scrClr\"")
            line = line.replace("""\"screenResolution\"""", "\"scrRes\"")
            line = line.replace("""\"deviceCategory\"""", "\"devCat\"")
            line = line.replace("""\"continent\"""", "\"cont\"")
            line = line.replace("""\"subContinent\"""", "\"subCont\"")
            line = line.replace("""\"country\"""", "\"cntry\"")
            line = line.replace("""\"metro\"""", "\"met\"")
            line = line.replace("""\"(not set)\"""", "\"n/a\"")
            line = line.replace("""\"(not provided)\"""", "\"n/a\"")
            line = line.replace("""\"networkDomain\"""", "\"netDom\"")
            line = line.replace("""\"latitude\"""", "\"lat\"")
            line = line.replace("""\"longitude\"""", "\"long\"")
            line = line.replace("""\"networkLocation\"""", "\"netLoc\"")
            line = line.replace("""\"pageviews\"""", "\"pView\"")
            line = line.replace(""",Not Socially Engaged,""", ",NotSocEng,")
            line = line.replace("""\"adwordsClickInfo\"""", "\"adClikInfo\"")
            line = line.replace("""\"criteriaParameters\"""", "\"critParam\"")
            line = line.replace("""\"Northern """, "\"North")
            line = line.replace("""\"Southern """, "\"South")
            line = line.replace("""\"Western """, "\"West")
            line = line.replace("""\"Eastern """, "\"East")
            line = line.replace("""\"unknown.unknown\"""", "\"n/a\"")
            line = line.replace("""\"source\"""", "\"src\"")
            output_file.write(line)
