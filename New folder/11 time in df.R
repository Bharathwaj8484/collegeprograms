library(dplyr)

# Sample data
df <- data.frame(group = c("A", "A", "A", "B", "B", "B"),
                 date = c("2022-04-01", "2022-04-01", "2022-04-02", "2022-04-01", "2022-04-02", "2022-04-02"),
                 time = c("10:00:00", "12:00:00", "08:00:00", "09:00:00", "10:00:00", "13:00:00"),
                 stringsAsFactors = FALSE)

# Convert to datetime format
df$datetime <- as.POSIXct(paste(df$date, df$time), format = "%Y-%m-%d %H:%M:%S")

# Calculate time difference with previous row for each group
df <- df %>% 
  arrange(group, datetime) %>% 
  group_by(group) %>% 
  mutate(time_diff = difftime(datetime, lag(datetime), units = "mins"))

# Print the result
print(df)
