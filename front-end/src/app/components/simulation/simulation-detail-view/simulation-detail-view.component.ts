import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute, ParamMap} from '@angular/router';
import {SimulationAPIService} from '../../../services/api/simulation/simulation-api.service';
import {Observable} from 'rxjs';
import {SimulationAPIResource} from '../../../models/simulation.models';
import {switchMap} from 'rxjs/operators';

@Component({
  selector: 'app-simulation-detail-view',
  templateUrl: './simulation-detail-view.component.html',
  styleUrls: ['./simulation-detail-view.component.scss']
})
export class SimulationDetailViewComponent implements OnInit {

  constructor(
    private activatedRoute: ActivatedRoute,
    private simulationAPIService: SimulationAPIService
  ) { }

  simulation$: Observable<SimulationAPIResource>;

  ngOnInit(): void {
    this.simulation$ = this.activatedRoute.paramMap.pipe(
      switchMap((params: ParamMap) => this.simulationAPIService.get(parseInt(params.get('id'), 10)))
    );
  }

}
