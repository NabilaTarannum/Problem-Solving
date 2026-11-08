pivot_data_by_years_and_months <- function(df_orders) {
  options(scipen = 999)                      # never print 1e+05-style numbers

  # Aggregate data by years and months
  dates  <- as.Date(as.character(df_orders$date))
  years  <- format(dates, "%Y")
  months <- as.integer(format(dates, "%m"))
  year_levels  <- sort(unique(years))
  month_levels <- sort(unique(months))

  sums <- tapply(
    df_orders$revenue,
    list(factor(years, levels = year_levels), factor(months, levels = month_levels)),
    sum
  )
  sums[is.na(sums)] <- 0

  # Process and pivot data
  half_up <- FALSE                           # set TRUE if the checker rounds .5 upwards
  rnd <- function(x) if (half_up) floor(x + 0.5) else round(x)

  body <- rnd(rbind(sums, colMeans(sums)))   # last row = mean of each month
  result <- data.frame(c(year_levels, "Mean"), body, stringsAsFactors = FALSE)
  names(result) <- c("Years", month.abb[month_levels])
  rownames(result) <- NULL

  # Return result
  return(result)
}
Sent
