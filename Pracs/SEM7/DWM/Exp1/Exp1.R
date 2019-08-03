# Assigning and auto-printing
x <- 10
x + 2
x - 2
x * 2

# Returns floating point 
x / 3

# Assigning strings
msg <- "hello"
print(msg)

# Vectors
a <- 10:30
a
b <- c(0.5,0.6)
b

# Matrices
c <- 1:3
d <- 6:9
e <- 6:8
cbind(c,d,e)
rbind(c,d,e)
matrix(1:6,2,3)

# Factors
x <- factor(c("fire","fire","water","water"))
x
table(x)
unclass(x)

# CSV Reading
pokemon <- read.csv("./pokemon.csv")
pokemon

# CSV read first few rows and structure
summary(pokemon)