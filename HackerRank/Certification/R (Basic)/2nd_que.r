#' Calculate the average temperature in cities by dates
#' @param df_data Data frame from 'csv' file
#' @return Data frame with average temperatures
calculate_average_temperature_in_cities_by_dates <- function(df_data) {

  if (is.null(df_data) || !is.data.frame(df_data)) return(data.frame())
  if (nrow(df_data) == 0L || ncol(df_data) < 2L) {
    return(data.frame(Date = character(0), stringsAsFactors = FALSE))
  }

  cities <- names(df_data)[-1]          

  date_chr <- substr(trimws(as.character(df_data[[1]])), 1L, 10L)

  vals <- df_data[, -1, drop = FALSE]
  vals[] <- lapply(vals, function(x) suppressWarnings(as.numeric(as.character(x))))

  u_dates <- sort(unique(date_chr))
  grp     <- factor(match(date_chr, u_dates), levels = seq_along(u_dates))

  out <- data.frame(Date = u_dates, stringsAsFactors = FALSE, check.names = FALSE)
  for (city in cities) {
    col <- vals[[city]]
    avg <- vapply(split(col, grp), function(v) {
      v <- v[!is.na(v)]
      if (length(v) == 0L) NA_real_ else mean(v)q
    }, numeric(1))
    out[[city]] <- round(unname(avg), 2)
  }

  rownames(out) <- NULL
  out
}
