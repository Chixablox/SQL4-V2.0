create or replace function transform_and_load2 (start_date DATE, end_date DATE)
returns void as $$

begin
	insert into sourcetable
	select * 
	from temptable
	where 
		not (
			(id is null and user_id is null and track is null and artist is null and genre is null and city is null
			and time is null and report_date is null and weekday is null) or report_date is null
		)
		and
		report_date between start_date and end_date;
end;
$$ language plpgsql;
