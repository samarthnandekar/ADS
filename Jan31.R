getwd()
setwd("C:/Users/samar/Downloads")

data <- read.table("ClassDataSheet1.csv",header = T,sep=',')

#--------   1) Min, Max, Median, Avg for GPA and YearofWorkExp

print(min(data$GPA));
print(max(data$GPA));
print(median(data$GPA));
print(mean(data$GPA));

print(min(data$Years.of.work.experience));
print(max(data$Years.of.work.experience));
print(median(data$Years.of.work.experience));
print(mean(data$Years.of.work.experience));

#-------   2) Find the mode of the Salary

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

result <- getmode(data$Latest.salary..per.year)
print(result)

#-------- 3) % of students having Co/op and not having Co/op


gotCoop <- data$Coops.Internships == 'Y';

gotCoopCount <- sum(gotCoop);

totalStudent <-length(gotCoop);

gotCoopCountPer <- gotCoopCount*100/totalStudent;

print(gotCoopCountPer)

notGottheCoop <- totalStudent - gotCoopCount;

notGottheCoopper <- notGottheCoop*100/totalStudent;

print(notGottheCoopper)
#---------- 4) No of students with more than 500 LinkedIn contacts

account <-data$Number.of.contacts.on.Linkedin > 500

forCount<-account==TRUE;  #why only true value is not comming in forcount.

print(sum(forCount));


#---------- 5) Find the Inter Quartile Range for the Expected Salalry Range?



iqrValur <- IQR(data$Expected.Salary.after.graduation);

print(iqrValur)



