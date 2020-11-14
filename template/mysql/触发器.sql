
-- 模板
DROP TRIGGER IF EXISTS trigger_name;
CREATE TRIGGER trigger_name
BEFORE INSERT|BEFORE DELETE|BEFORE UPDATE|AFTER INSERT|AFTER DELETE|AFTER UPDATE
ON tb_name FOR EACH ROW 
BEGIN
	trigger_stmt
END;
$$
delimiter ;

-- 案例

-- 专业户触发器
delimiter $$
DROP TRIGGER IF EXISTS trigger_in_special_report;
CREATE TRIGGER trigger_in_special_report
AFTER INSERT
	ON special_account_report
	FOR EACH ROW
BEGIN
	IF EXISTS (
		SELECT 1
		FROM report_record
		WHERE account = new.saccno
	) THEN
		UPDATE report_record
		SET repor_channel = 'API', account_type = '专业户', apply_time=new.daccbegindate, CODE = new.CODE, STATUS = new.STATUS, msg = new.msg, create_time = new.start_time, last_time = new.end_time
		WHERE account = new.saccno;
	ELSE 
		INSERT INTO report_record (account,apply_time, repor_channel, account_type,  CODE
			, STATUS, msg, create_time, last_time)
		VALUES (new.saccno, new.daccbegindate,'API', '专业户', new.CODE
			, new.STATUS, new.msg, new.start_time, new.end_time);
	END IF;
end;

$$
delimiter ;





