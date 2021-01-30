import { Component } from '@angular/core';
import {SimulationAPIService} from '../../../services/api/simulation/simulation-api.service';

@Component({
  selector: 'app-simulation-list-view',
  templateUrl: './simulation-list-view.component.html',
  styleUrls: ['./simulation-list-view.component.scss']
})
export class SimulationListViewComponent {
  simulations$ = this.simulationAPIService.list();

  constructor(private simulationAPIService: SimulationAPIService) {}
}
