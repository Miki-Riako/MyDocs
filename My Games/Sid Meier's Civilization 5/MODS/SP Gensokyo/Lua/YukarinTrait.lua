function GensokyoTrait(playerID)
	local player = Players[playerID]

	if player == nil then
		print ("No players")
		return
	end

	if player:IsBarbarian() or player:IsMinorCiv() then
		print ("Minors are Not available!")
    	return
	end

	if player:GetNumCities() <= 0 then
		print ("No Cities!")
		return
	end

	if GameInfo.Leader_Traits{
        LeaderType = GameInfo.Leaders[player:GetLeaderType()].Type,
        TraitType = "TRAIT_UNITED_GENSOKYO"
    }() then
		for pCity in player:Cities() do
		    if pCity ~= nil then
				local Cityname = pCity:GetName()
				local CityFaith = pCity:GetYieldRate(YieldTypes.YIELD_FAITH)
				local FaithRate = 0
				local MountainCount = 0
				pCity:SetNumRealBuilding(GameInfoTypes["BUILDING_TB_UNITED_GENSOKYO_SCIENCE_BONUS"], 0)
				pCity:SetNumRealBuilding(GameInfoTypes["BUILDING_TB_UNITED_GENSOKYO_PRODUCTION_BONUS"], 0)
				print ("Gensokyo City:"..Cityname.."Faith:"..CityFaith)
				if CityFaith < 25 then
					print ("Faith Too Low!")
				else
					FaithRate = math.floor(CityFaith/25)
					print ("Faith to Science for Gensokyo! Rate:"..FaithRate)
				end
				for i = 0, pCity:GetNumCityPlots() - 1, 1 do
					local plot = pCity:GetCityIndexPlot(i)
					if plot and plot:GetOwner() == playerID and plot:IsMountain() then
						MountainCount = MountainCount + 1
					end
				end
				if FaithRate >= 1 then
					pCity:SetNumRealBuilding(GameInfoTypes["BUILDING_TB_UNITED_GENSOKYO_SCIENCE_BONUS"], FaithRate)
				end
				if MountainCount >= 1 then
					pCity:SetNumRealBuilding(GameInfoTypes["BUILDING_TB_UNITED_GENSOKYO_PRODUCTION_BONUS"], MountainCount)
				end
				print ("Gensokyo UA!")
			end
		end
	end
end---------Function End
GameEvents.PlayerDoTurn.Add(GensokyoTrait)
