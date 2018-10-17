public enum Rank
{
	deux (2),
	trois (3),
	quatre (4),
	cinq (5),
	six (6),
	sept (7),
	huit (8),
	neuf (9),
	dix (10),
	valet (10),
	dame (10),
	roi (10),
	as (20);

	int  value;							//define 1st element
	Rank(int v) { value = v; }			//setter
	int  value () {return value; }		//getter
}
