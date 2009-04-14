<ScreenSpec namespace="IronMacro.PokerStars">
	<Enum name="Suit">
		<Elem name="Heart" />
		<Elem name="Diamond" />
		<Elem name="Spade" />
		<Elem name="Club" />
	</Enum>
	
	<Class name="Card">
		<Prop name="Value" type="int" />
		<Prop name="Suit" type="Suit" />
	</Class>
	
	<Class name="Table">
		<Prop name="Hole1" type="Card" />
		<Prop name="Hole2" type="Card" />
		<Trigger name="HoleCardsDealt" on="appear" />
		
		<Prop name="Flop1" type="Card" />
		<Prop name="Flop2" type="Card" />
		<Prop name="Flop3" type="Card" />
		<Prop name="Turn"  type="Card" />
		<Prop name="River" type="Card" />
		<Trigger name="FlopDealt"  on="appear" />
		<Trigger name="TurnDealt"  on="appear" />
		<Trigger name="RiverDealt" on="appear" />
	</Class>
</ScreenSpec>
